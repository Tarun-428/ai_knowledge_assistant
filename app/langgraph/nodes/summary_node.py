from app.ingestion.vector_store import get_vector_store
from app.rag.generator import get_llm

from langchain_core.documents import Document
from langchain_classic.chains.summarize import load_summarize_chain
from langchain_core.prompts import ChatPromptTemplate

SUMMARY_PROMPT = ChatPromptTemplate.from_template( """
Summarize the following document clearly.

Format the answer using:

Title
Key Points
Important Concepts
Conclusion

Text:
{text}
"""
)

def summary_node(state):

    history = state.get("history", "")

    vectorstore = get_vector_store()

    raw_docs = vectorstore.get()
    metadatas = raw_docs["metadatas"]

    if not metadatas:
        return {"answer": "No documents found to summarize."}

    latest_source = max(
        metadatas,
        key=lambda x: x.get("timestamp", 0)
    )["source"]

    specific_raw = vectorstore.get(where={"source": latest_source})

    chunks = specific_raw["documents"][:6]

    combined_docs = []

    for i in range(0, len(chunks), 3):
        combined_text = "\n\n".join(chunks[i:i+3])
        combined_docs.append(Document(page_content=combined_text))

    print("Docs sent to LLM:", len(combined_docs))

    llm = get_llm()

    chain = load_summarize_chain(
        llm,
        chain_type="map_reduce",
        map_prompt=SUMMARY_PROMPT,
    )
    print('llm calling')
    summary = chain.invoke(combined_docs)
    print('llm stopped')
    # print(summary["output_text"])
    return {
        "answer": summary["output_text"],
        "history": history
    }