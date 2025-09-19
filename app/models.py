from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.database import Base
import datetime

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)  
    done = Column(Boolean, default=False)
    date_created = Column(DateTime, default=datetime.datetime.utcnow)
