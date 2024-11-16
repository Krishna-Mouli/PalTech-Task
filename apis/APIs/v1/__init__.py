from fastapi import APIRouter
from .filesapis import router as files_router
from .resumeapis import router as resume_router

api_versionv1_router = APIRouter()

api_versionv1_router.include_router(files_router, prefix="/files", tags = ["files"])
api_versionv1_router.include_router(resume_router, prefix="/resume", tags = ["resume"])