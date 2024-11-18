from fastapi import UploadFile
from ..database import AzureBlobServices, PineConeService, TableRepository
from ..ai import OpenAIServices
from utils import read_from_file, chunk_content, PromptTemplate
from models import ChunkingTypes, ExtractorTypes
from data import Files
from dataclasses import asdict
import logging

from typing import List
import asyncio
import uuid
import json


class Ingestion:
    def __init__(self):
        self._azure_storage_service = AzureBlobServices()
        self._openai_service = OpenAIServices()
        self._pinecone_service = PineConeService()
        self._prompt_template_service = PromptTemplate()
        self._azuretableserviceclient = TableRepository(Files)

    async def Upload_and_Vectorize(self, file_bytes: bytes, app_id: str, filename: str, file: UploadFile, file_extension: str):
        #uploading file to google cloud service
        try:            
            await self._azure_storage_service.init()
            await self._azuretableserviceclient.init()
            public_url = await self._azure_storage_service.upload_file(app_id = app_id, blob_name = filename, file_stream = file)
        except Exception as e:
            return {"file": filename, "status": "failed at uploading to azure blob container", "error": str(e)}
        
        #calling exraction service
        try:
            content = ""
            if (file_extension == ".pdf"):
                content = read_from_file(ExtractorTypes.pdf, file_bytes)            
        except Exception as e:
            return {"file":filename, "status": "failed at extracting content", "error": str(e)}
        
        await self.process_resume(content = content, app_id = app_id, filename = filename, url = public_url)

        chunks = chunk_content(chunking_type = ChunkingTypes.Recursive, text = content)

        try:
            vectors = await self.process_chunks(chunks = chunks, filename = filename, app_id = app_id, public_url = public_url)
        except Exception as e:
            return {"file": filename, "status": "failed at creating vectors", "error": str(e)}
        
        try:
            self._pinecone_service.upsert_vectors(vectors)
        except Exception as e:
            return {"file": filename, "status": "failed at uploading vectors", "error": str(e)}
        
        return {"file":filename, "status":"Completely Processd successfully"}


    async def process_chunks(self, chunks: List[str], filename: str, app_id: str, public_url: str):        
        embedding_tasks = []
        for chunk in chunks:
            task = self._openai_service.EmbeddingsOpenAI(text = chunk)
            embedding_tasks.append(task)
        vectors = await asyncio.gather(*embedding_tasks)       
        return [{
            "id": str(uuid.uuid4()),
            "values": vector,
            "metadata": {
                "filename": filename,
                "appid": app_id,
                "filepath": public_url,
                "chunk_content": chunk
            }
        } for vector, chunk in zip(vectors, chunks)]   


    async def process_resume(self, content: str, app_id: str, filename: str, url: str):
        try:
            prompts = self._prompt_template_service.create_a_prompt_template(content = content, promptType = "summary")
            response = await self._openai_service.ChatCompletion(user_prompt=prompts["user_prompt"], 
                                                             system_prompt=prompts["system_prompt"],
                                                             json_mode = True) 
            AIresponse = json.loads(response)
            file_data = Files(
                PartitionKey = app_id,
                filename= filename,
                filepath= url,
                uploadedby="Test User PALTECH",
                fileid= "PALTECH-001",
                filesource="LinkedIn",
                username="Test User",
                resumecontent=content,
                resumesummary=AIresponse['summary'],
                personaldetails=AIresponse['personaldetails'],
                skills=AIresponse['skills'],
                professionalexperience=AIresponse['professionalexperience'],
                educationalbackground=AIresponse['educationalbackground'],
                certifications=AIresponse['certifications'],
                achievements=AIresponse['achievements'],
                interests=AIresponse['interests'],
            )
            files_dict = dict(file_data)
            await self._azuretableserviceclient.upsert_async(files_dict)   
        except Exception as e:
            logging.error(f"An error occurred while processing file {e}")
