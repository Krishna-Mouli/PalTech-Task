import logging
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from typing import List
import os
from services import Chat, ResumeServices
from data import SearchRequest
import json

router = APIRouter()

@router.post("/sourceid/{sourceid}/resumeid/{resumeid}/conversationid/{conversationid}/converse", description = "use this to converse with a partiular resume, which has a unique conversationID and so on." )
async def chat_resumes(sourceid: str, resumeid: str, conversationid:str, req: SearchRequest):   
    try:                                        
        _chat = Chat(resumeid = resumeid, convoid = conversationid, sourceid = sourceid)
        resp = await _chat.converse_init(convo_id = conversationid, resumeid = resumeid, question = req.searchrequest, sourceid = sourceid)               
        final = {"content": resp}
        return JSONResponse(
            status_code = 200,
            content = final
        )
    except Exception as e:
        return JSONResponse(
            status_code = 500,
            content = f"{str(e)}"
        )
    
@router.post("/sourceid/{sourceid}/resumeid/{resumeid}/conversationid/{conversationid}/resetchat", description = "reset an ongoing conversation")
async def reset_chat_resumes(sourceid: str, resumeid: str, conversationid:str):   
    try:                                        
        _chat = Chat(resumeid = resumeid, convoid = conversationid, sourceid = sourceid)
        resp = await _chat.reset_conversation(resumeid = resumeid, sourceid = sourceid)               
        final = {"content": resp}
        return JSONResponse(
            status_code = 200,
            content = final
        )
    except Exception as e:
        return JSONResponse(
            status_code = 500,
            content = f"{str(e)}"
        )
    

@router.get("/sourceid/{sourceid}/resumeid/{resumeid}/getdetails", description = "get details about a particular resume")
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


@router.get("/sourceid/{sourceid}/resumeid/{resumeid}/getquestions", description = "get the questions related to a particular resume and candidate")
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
