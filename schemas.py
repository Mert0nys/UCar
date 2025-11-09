from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class IncidentStatus(str, Enum):
    open = "open"
    in_progress = "in_progress"
    resolved = "resolved"
    closed = "closed"

class IncidentBase(BaseModel):
    description: str
    status: IncidentStatus
    source: str

class IncidentCreate(IncidentBase):
    pass

class Incident(IncidentBase):
    id: int
    created_at: datetime 
   
