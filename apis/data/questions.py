from pydantic import BaseModel, Field
from .baseentity import BaseEntity

class Questionnaire(BaseEntity):
    introductory: str
    experience: str
    technical: str
    education: str
    extra: str
    interests: str
    url: str
    filename: str
