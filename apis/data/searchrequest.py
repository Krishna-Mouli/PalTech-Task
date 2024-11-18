from pydantic import BaseModel

class SearchRequest(BaseModel):
    searchrequest: str