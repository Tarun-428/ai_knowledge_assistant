from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from app.rag.retriever import retrieve_documents
from app.rag.prompts import RAG_PROMPT
from app.rag.generator import get_llm


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def get_rag_chain():

    retriever = retrieve_documents()
    llm = get_llm()

    chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough(),
        }
        | RAG_PROMPT
        | llm
        | StrOutputParser()
    )

    return chain