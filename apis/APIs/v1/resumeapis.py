import logging
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from typing import List
import os
from services import Chat
from data import SearchRequest

router = APIRouter()

@router.post("/apps/{appid}/conversations/{conversationid}")
async def chat_resumes(appid: str, conversationid: str, req: SearchRequest):   
    try:
        app_id = "f8b7c3a1-9d2e-4f5b-8c7a-6d4e3f2b1a9c"                                 
        _chat = Chat(appid = appid, convoid = conversationid)
        resp = await _chat.converse_init(convo_id = conversationid, app_id = appid, question = req.searchrequest)         
        return JSONResponse(
            status_code = 200,
            content = resp
        )
    except Exception as e:
        return JSONResponse(
            status_code = 500,
            content = f"{str(e)}"
        )
    
