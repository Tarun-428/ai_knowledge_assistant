from langchain_chroma import Chroma

from app.ingestion.embedder import get_embedding_model


CHROMA_DIR = "chroma_db"
COLLECTION_NAME = "company_documents"


def get_vector_store():
    """
    Create or load Chroma vector store
    """

    embeddings = get_embedding_model()

    vector_store = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=CHROMA_DIR,
    )
    return vector_store