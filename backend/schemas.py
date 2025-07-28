from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class RunBase(BaseModel):
    date: datetime
    distance: float
    duration: int
    heart_rate: Optional[int] = None
    location: Optional[str] = None
    notes: Optional[str] = None

class RunCreate(RunBase):
    pass

class RunUpdate(RunBase):
    pass

class Run(RunBase):
    id: int

    class Config:
        from_attributes = True  # для SQLAlchemy