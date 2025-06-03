# from pydantic import BaseModel

# class Task(BaseModel):
#     title: str
#     description: str
#     done: bool = False

from sqlalchemy import Column, Integer, String
from .database import Base
# from database import Base #For Test

class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "dcp_api"}  # ✅ ระบุ schema ตรงนี้

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
