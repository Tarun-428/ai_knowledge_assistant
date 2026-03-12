from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

# from app.rag.retriever import get_retriever
from app.rag.generator import get_llm
from app.rag.prompts import RAG_PROMPT
from app.rag.retriever import retrieve_documents

from app.guardrails.input_validation import validate_input
from app.guardrails.prompt_injection import detect_prompt_injection
from app.guardrails.grounding_check import check_grounding
from app.guardrails.pii_filter import filter_pii

def validate_question(x):
    question = validate_input(x["question"])

    if detect_prompt_injection(question):
        raise ValueError("Prompt injection detected")

    x["question"] = question
    return x

def retrieve_context(x):
    docs = retrieve_documents(x["question"])

    x["docs"] = docs
    x["context"] = format_docs(docs)

    return x

def guard_output(x):

    answer = x["answer"]
    docs = x["docs"]

    grounded = check_grounding(answer, docs)

    if not grounded:
        answer = "The answer could not be reliably grounded in company documents."

    answer = filter_pii(answer)

    x["answer"] = answer

    return x
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def get_conversational_rag_chain():

    llm = get_llm()

    chain = (

        RunnableLambda(validate_question)

        | RunnableLambda(retrieve_context)

        | {
            "context": lambda x: x["context"],
            "question": lambda x: x["question"],
            "history": lambda x: x["history"],
            "docs": lambda x: x["docs"],
        }

        | RAG_PROMPT

        | llm

        | StrOutputParser()

        | RunnableLambda(lambda answer: {"answer": answer})

    )

    return chain