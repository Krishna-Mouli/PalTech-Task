import logging
from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from typing import List
import os
from Services import Ingestion
import asyncio

router = APIRouter()