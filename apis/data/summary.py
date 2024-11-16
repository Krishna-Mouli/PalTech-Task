from pydantic import BaseModel, Field
from .baseentity import BaseEntity

class Summary(BaseEntity):
    fileid: str
    username: str
    resumesummary: str