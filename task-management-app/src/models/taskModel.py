from sqlalchemy import Column,Integer, String, Boolean
from src.config.db import Base

class TaskModel(Base):
    __tablename__ = "user_tasks"

    id = Column(Integer,primary_key=True)
    title = Column(str)
    description = Column(str)
    is_completed = Column(Boolean,default=False)