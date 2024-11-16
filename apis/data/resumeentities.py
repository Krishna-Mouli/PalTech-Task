from pydantic import BaseModel, Field
from .baseentity import BaseEntity

class ResumeEntities(BaseEntity):
    fileid: str
    username: str
    personaldetails: str
    skills: str
    professionalexperience: str
    educationalbackground: str
    certifications: str