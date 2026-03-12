from fastapi import APIRouter
from pydantic import BaseModel

from app.rag.conversational_chain import get_conversational_rag_chain
# from app.memory.conversation_memory import memory_store
from app.memory.history_formatter import format_history
from fastapi.responses import StreamingResponse
from app.guardrails.grounding_check import check_grounding
from app.guardrails.pii_filter import filter_pii
from app.rag.retriever import retrieve_documents
from app.auth.auth_middleware import get_current_user
from fastapi import Depends,Request
router = APIRouter()
import uuid

class ChatRequest(BaseModel):
    question: str
    conversation_id: str

class ChatResponse(BaseModel):
    answer: str

@router.post("/ask", response_model=ChatResponse)
async def chat(request: ChatRequest,user=Depends(get_current_user)):

    chain = get_conversational_rag_chain()

    history = memory_store.get_history(request.conversation_id)
    formatted_history = format_history(history)
    role = user["role"]
    
    docs = retrieve_documents(request.question)


    raw_response = chain.invoke({
        "question": request.question,
        "history": formatted_history
    })

    if isinstance(raw_response, dict):
        result = raw_response.get("answer", "")
    else:
        result = raw_response

    if not check_grounding(result, docs):
        result = "The answer could not be grounded in company documents."

    result = filter_pii(result)

    memory_store.add_message(
        request.conversation_id,
        "user",
        request.question
    )

    memory_store.add_message(
        request.conversation_id,
        "assistant",
        result
    )

    return ChatResponse(answer=result)




from app.langgraph.graph import graph
from app.services import memory_store



from app.rag.generator import get_llm
from app.rag.prompts import RAG_PROMPT
import json
import asyncio

@router.post("/stream")
async def chat_stream(request: ChatRequest,req:Request,user=Depends(get_current_user)):
    role = user["role"]

    # get redis conversation history
    history = memory_store.get_history(request.conversation_id)

    formatted_history = format_history(history)

    print("streaming started")

    async def event_generator():

        full_answer = ""

        result = graph.invoke({
            "question": request.question,
            "history": formatted_history
        })

        # print("GRAPH RESULT:", result.keys())
  
        if "prompt" in result:
            prompt = result["prompt"]
            llm = get_llm(streaming=True)
            messages = prompt.to_messages()
            async for chunk in llm.astream(messages):
                if await req.is_disconnected():
                    print("Client disconnected")
                    break
                token = chunk.content
                if token:
                    full_answer += token

                    yield f"data: {json.dumps({'token': token})}\n\n"

        elif "answer" in result:
            answer = result["answer"]
            full_answer += answer
 
            for i in range(0, len(answer), 5):
                chunk = answer[i:i+5]
                yield f"data: {json.dumps({'token': chunk})}\n\n"
                await asyncio.sleep(0.01)
        memory_store.add_message(
            request.conversation_id,
            role,
            request.question
        )

        memory_store.add_message(
            request.conversation_id,
            role,
            full_answer
        )

        yield "data: [DONE]\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no"
        }
    )