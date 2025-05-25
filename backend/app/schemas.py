from pydantic import BaseModel
from datetime import datetime

class StatusCreate(BaseModel):
    service_name: str
    status: str

class Status(StatusCreate):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True
