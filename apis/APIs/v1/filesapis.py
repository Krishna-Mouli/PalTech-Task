import logging
from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from typing import List
import os
from services import Ingestion

router = APIRouter()
ALLOWED_EXTENSIONS = {".pdf"}
MAX_FILE_SIZE = 10 * 1024 * 1024

@router.post("/sourceid/{sourceid}/resumeid/{resumeid}/ingest")
async def index_resumes(sourceid: str, resumeid: str, file: UploadFile = File(...)):                           
    extension = os.path.splitext(file.filename)[1]
    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail=f"File type {extension} is not allowed.")
    content = await file.read()
    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail=f"File {file.filename} exceeds the size limit. Keep it under 5Mb")           
    _ingestion = Ingestion()
    resp = await _ingestion.Upload_and_Vectorize(file_bytes = content, sourceid = sourceid, resumeid = resumeid, filename=file.filename, file = file, file_extension = extension)           
    return JSONResponse(
        status_code = 200,
        content = f"Files processed successfully.\n details: {resp}"
    )
    
