from pydantic import BaseModel, Field
from .baseentity import BaseEntity

class Files(BaseEntity):
    filename: str
    filepath: str
    uploadedby: str
    fileid: str
    filesource: str
    username: str
    resumecontent: str
    resumesummary: str
    personaldetails: str
    skills: str
    professionalexperience: str
    educationalbackground: str
    certifications: str
    achievements: str
    interests: str
