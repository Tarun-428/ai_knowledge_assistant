from fastapi import APIRouter, UploadFile, File
import shutil
from pathlib import Path

from app.ingestion.pipeline import ingest_document
from app.auth.auth_middleware import get_current_user
from fastapi import Depends

router = APIRouter()

UPLOAD_DIR = Path("uploaded_docs")
UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/documents/upload")
async def upload_document(file: UploadFile = File(...),user=Depends(get_current_user)):

    file_path = UPLOAD_DIR / file.filename
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)   

    result = ingest_document(str(file_path),user["user_id"])
    return result