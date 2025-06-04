from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    name: str
    age: int

class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    id: int

    class Config:
        # orm_mode = True
        from_attributes = True  # ใช้ใน Pydantic v2

class UpdateUser(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
