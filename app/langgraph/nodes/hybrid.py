
from rank_bm25 import BM25Okapi
from app.ingestion.vector_store import get_vector_store
import pickle

def bm25_retrieve(query, k=5):

    with open("bm25_index.pkl", "rb") as f:
        bm25, texts, chunks = pickle.load(f)

    tokenized_query = query.split()

    scores = bm25.get_scores(tokenized_query)

    ranked = sorted(
        zip(chunks, scores),
        key=lambda x: x[1],
        reverse=True
    )

    docs = [doc for doc, _ in ranked[:k]]

    return docs

def hybrid_search(query, k=20):

    vector_store = get_vector_store()

    vector_docs = vector_store.similarity_search(
        query,
        k=k
    )

    # BM25 search
    bm25_docs = bm25_retrieve(query, k)
    # print("bm25:",bm25_docs)
    combined = vector_docs + bm25_docs

    # remove duplicates
    unique = {}
    for doc in combined:
        unique[doc.page_content] = doc
    # print("unique",unique)
    return list(unique.values())


from sentence_transformers import CrossEncoder

reranker = CrossEncoder(
    "BAAI/bge-reranker-base"
)

def rerank_documents(query, docs, top_k=5):

    pairs = [
        (query, doc.page_content)
        for doc in docs
    ]

    scores = reranker.predict(pairs)

    ranked = sorted(
        zip(docs, scores),
        key=lambda x: x[1],
        reverse=True
    )

    return [doc for doc, _ in ranked[:top_k]]

def retrieve_documents(query):

    # Step 1: hybrid retrieval
    docs = hybrid_search(query, k=20)

    # Step 2: rerankretrieve_documents
    top_docs = rerank_documents(query, docs, top_k=5)

    return top_docs