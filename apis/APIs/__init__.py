from fastapi import APIRouter
from .v1 import api_versionv1_router as v1_router

api_version_router = APIRouter()

api_version_router.include_router(v1_router, prefix="/api/v1", tags = ["v1"])