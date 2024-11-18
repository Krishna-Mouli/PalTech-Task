from pydantic import BaseModel
from typing import List
class Vectors(BaseModel):
    vector_id: str
    app_id: str
    chunk_content: str
    filename: str
    filepath: str
    score: float
    values: List[float]
