from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import Docx2txtLoader
from langchain_community.document_loaders import TextLoader


def load_document(file_path: str):
    """
    Load document based on file type
    """

    path = Path(file_path)
    suffix = path.suffix.lower()

    if suffix == ".pdf":
        loader = PyPDFLoader(file_path)

    elif suffix == ".docx":
        loader = Docx2txtLoader(file_path)

    elif suffix == ".txt":
        loader = TextLoader(file_path)

    else:
        raise ValueError(f"Unsupported file type: {suffix}")

    documents = loader.load()

    return documents