from fastapi import UploadFile
from ..database import AzureBlobServices, PineConeService
from ..ai import OpenAIServices
from utils import read_from_file, chunk_content
from models import ChunkingTypes, ExtractorTypes

from typing import List
import asyncio
import uuid


class Ingestion:
    def __init__(self):
        self._azure_storage_service = AzureBlobServices()
        self._openai_service = OpenAIServices()
        self._pinecone_service = PineConeService()

    async def Upload_and_Vectorize(self, file_bytes: bytes, app_id: str, filename: str, file: UploadFile, file_extension: str):
        #uploading file to google cloud service
        try:
            public_url = await self._azure_storage_service.upload_file(app_id = app_id, filename = filename, file = file)
        except Exception as e:
            return {"file": filename, "status": "failed at uploading to azure blob container", "error": str(e)}
        
        #calling exraction service
        try:
            content = ""
            if (file_extension == ".pdf"):
                content = read_from_file(ExtractorTypes.pdf, file_bytes)            
        except Exception as e:
            return {"file":filename, "status": "failed at extracting content", "error": str(e)}

        chunks = chunk_content(chunking_logic = ChunkingTypes.Recursive, content = content)

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
            task = self._openai_service.EmbeddingsOpenAI(text=chunk)
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