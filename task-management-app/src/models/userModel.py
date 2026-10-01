from sqlalchemy import Column, String, Integer
from src.config.db import Base

class UserModel(Base):
    __tablename__ = "user_table"


    id = Column(Integer,primary_key=True)
    name = Column(String)
    username = Column(String,nullable=False,unique=True)
    hash_password = Column(String,nullable=False)
    email = Column(String,unique=True)
