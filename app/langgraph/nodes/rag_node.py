# from app.rag.retriever import retrieve_documents
from app.langgraph.nodes.hybrid import retrieve_documents
from app.rag.generator import get_llm
from app.rag.prompts import RAG_PROMPT


def rag_node(state):

    question = state["question"]
    history = state.get("history", "")

    docs = retrieve_documents(question)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    prompt = RAG_PROMPT.invoke({
        "context": context,
        "question": question,
        "history": history
    })
    # print("prompt: ",prompt)
    return {
        "prompt": prompt,
        "docs": docs,
        "history": history
    }