from langchain_huggingface import HuggingFaceEmbeddings


def get_embedding_model():
    """
    Local embedding model using SentenceTransformers
    """

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return embeddings