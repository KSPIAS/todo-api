# from typing import List
# from models import Task

# # จำลองฐานข้อมูลด้วย list
# todo_list: List[Task] = []


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ตั้งค่าการเชื่อมต่อ
DATABASE_URL = "postgresql://postgres:P%40ssw0rd@localhost:5433/fastapi_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
