from app.ingestion.vector_store import get_vector_store
from app.rag.reranker import reranker


def retrieve_documents(query: str,):

    vector_store = get_vector_store()

    docs = vector_store.similarity_search(
        query,
        k=20
    )

    reranked_docs = reranker.rerank(query, docs,top_k=4)
        
    return reranked_docs
