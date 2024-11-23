from pydantic import BaseModel, Field
from datetime import datetime
from uuid import uuid4
from typing import Optional

class BaseEntity(BaseModel):
    PartitionKey: Optional[str] = None
    RowKey: str = None
    timestamp: Optional[datetime] = Field(default=None, exclude=True)
    etag: Optional[str] = Field(default=None, exclude=True)