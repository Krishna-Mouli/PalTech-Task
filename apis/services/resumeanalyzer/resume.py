from ..database import TableRepository
from data import Files, Questionnaire
import json
import logging

class ResumeServices():
    def __init__(self, sourceid, resumeid):
        self.sourceid = sourceid
        self.resumeid = resumeid
        self._tableservice = TableRepository(Files)
        self._tableservice_questions = TableRepository(Questionnaire)

    async def get_resume_details(self):
        await self._tableservice.init()
        resp = await self._tableservice.query_async(filter_query = f"PartitionKey eq '{self.sourceid}' and RowKey eq '{self.resumeid}'")
        return resp
    
    async def get_question_details(self):       
        await self._tableservice_questions.init()
        resp = await self._tableservice_questions.query_async(filter_query = f"PartitionKey eq '{self.sourceid}' and RowKey eq '{self.resumeid}'")
        formatted_resp = []
        try:
            for entity in resp:
                formatted_entity = {
                    "PartitionKey": entity.get("PartitionKey"),
                    "RowKey": entity.get("RowKey"),
                    "introductory": json.loads(entity.get("introductory", "[]")),
                    "experience": json.loads(entity.get("experience", "[]")),
                    "technical": json.loads(entity.get("technical", "[]")),
                    "education": json.loads(entity.get("education", "[]")),
                    "extra": json.loads(entity.get("extra", "[]")),
                    "interests": json.loads(entity.get("interests", "[]"))
                }
                formatted_resp.append(formatted_entity)

            return formatted_resp
        except Exception as e:
            logging.error(f"{str(e)}")