import logging
from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from typing import List
import os
from services import Ingestion

router = APIRouter()
ALLOWED_EXTENSIONS = {".pdf", ".docx"}
MAX_FILE_SIZE = 10 * 1024 * 1024

@router.post("/ingest")
async def index_resumes(file: UploadFile = File(...)):   
    app_id = "f8b7c3a1-9d2e-4f5b-8c7a-6d4e3f2b1a9c"                    
    extension = os.path.splitext(file.filename)[1]
    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail=f"File type {extension} is not allowed.")
    content = await file.read()
    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail=f"File {file.filename} exceeds the size limit. Keep it under 5Mb")           
    _ingestion = Ingestion()
    resp = await _ingestion.Upload_and_Vectorize(file_bytes = content, app_id = app_id, filename=file.filename, file = file, file_extension = extension)           
    return JSONResponse(
        status_code = 200,
        content = f"Files processed successfully.\n details: {resp}"
    )
    
