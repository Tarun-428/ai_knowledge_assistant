from app.ingestion.loader import load_document
from app.ingestion.chunker import chunk_documents
from app.ingestion.vector_store import get_vector_store
import time
from rank_bm25 import BM25Okapi
import pickle

def ingest_document(file_path: str, user_id: str):
    # 1. Load the document
    documents = load_document(file_path)
    print(user_id)
    for doc in documents:
        doc.metadata["user_id"] = user_id
        doc.metadata["timestamp"] = time.time()
        if "source" not in doc.metadata:
            doc.metadata["source"] = file_path

    # print(documents)
    chunks = chunk_documents(documents)
    texts = [chunk.page_content for chunk in chunks]
    tokenized = [text.split() for text in texts]

    bm25 = BM25Okapi(tokenized)

    with open("bm25_index.pkl", "wb") as f:
        pickle.dump((bm25, texts,chunks), f)
    vector_store = get_vector_store()
    vector_store.add_documents(chunks)

    return {
        "status": "success",
        "chunks_indexed": len(chunks),
        "source": file_path
    }