import datetime
import uuid

from pydantic import BaseModel
from typing import Optional

# ---------------------------------
# アプリケーションで使用するスキーマを定義
# ---------------------------------
class ProjectBase(BaseModel):
    project_name: str
    description: Optional[str] = None

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    project_id: uuid.UUID
    created_datetime: datetime.datetime

    class Config:
        orm_mode = True

# class UserBase(BaseModel):
#     name: str
#     password: str

# class UserCreate(UserBase):
#     pass

# class User(BaseModel):
#     user_id: uuid.UUID
#     is_active: bool
#     create_datetime: datetime.datetime

#     class Config:
#         orm_mode = True


# class Token(BaseModel):
#     access_token: str
#     token_type: str