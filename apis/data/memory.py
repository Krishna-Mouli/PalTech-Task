from pydantic import BaseModel, Field
from .baseentity import BaseEntity
from typing import List

class MemorySummarizer(BaseEntity):        
    summarizedcontent: str = Field(default=None) 
    conversationid: str = Field(default=None)
    userid: str = Field(default=None)
    