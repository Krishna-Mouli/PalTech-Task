from pydantic import BaseModel
from typing import List
class Vectors(BaseModel):
    vector_id: str
    resumeid: str
    sourceid: str
    chunk_content: str
    filename: str
    filepath: str
    score: float
    values: List[float]
