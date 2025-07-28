from sqlalchemy import Column, Integer, Float, String, DateTime
from backend.database import Base

class Run(Base):
    __tablename__ = "runs"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, index=True)
    distance = Column(Float)  # км
    duration = Column(Integer)  # секунды
    heart_rate = Column(Integer, nullable=True)
    location = Column(String, nullable=True)
    notes = Column(String, nullable=True)