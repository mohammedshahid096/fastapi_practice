from sqlalchemy import Column,Integer, String, Boolean,ForeignKey,DateTime
from src.config.db import Base
from datetime import datetime

class TaskModel(Base):
    __tablename__ = "user_tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    is_completed = Column(Boolean,default=False)
    user_id = Column(Integer,ForeignKey("user_table.id",ondelete="CASCADE"))
    created_at = Column(DateTime,default=datetime.utcnow,  nullable=False)
    updated_at = Column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow,nullable=False)