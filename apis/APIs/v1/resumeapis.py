import logging
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from typing import List
import os
from services import Chat, ResumeServices
from data import SearchRequest

router = APIRouter()

@router.post("/sourceid/{sourceid}/resumeid/{resumeid}/conversations/{conversationid}/converse")
async def chat_resumes(sourceid: str, resumeid: str, conversationid:str, req: SearchRequest):   
    try:                                        
        _chat = Chat(appid = resumeid, convoid = conversationid)
        resp = await _chat.converse_init(convo_id = conversationid, app_id = resumeid, question = req.searchrequest)         
        return JSONResponse(
            status_code = 200,
            content = resp
        )
    except Exception as e:
        return JSONResponse(
            status_code = 500,
            content = f"{str(e)}"
        )
    

@router.get("/sourceid/{sourceid}/resumeid/{resumeid}/getdetails")
async def get_resume_details(sourceid: str, resumeid: str ):
    try:
        _resumeservice = ResumeServices(sourceid, resumeid)
        resp = await _resumeservice.get_resume_details()
        return JSONResponse(
            status_code=200,
            content=resp
        )
    except Exception as e:
        JSONResponse(
            status_code = 500,
        )


@router.get("/sourceid/{sourceid}/resumeid/{resumeid}/getquestions")
async def get_resume_questions(sourceid: str, resumeid: str):
    try:
        _resumeservice = ResumeServices(sourceid, resumeid)
        resp = await _resumeservice.get_question_details()
        return JSONResponse(
            status_code=200,
            content=resp
        )
    except Exception as e:
        JSONResponse(
            status_code = 500,
        )
