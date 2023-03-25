from enum import Enum
from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel

class Role(str, Enum):
    student = "student"
    admin = "admin"
    user = "user"

class Gender(str, Enum):
    male = "male"
    female = "female"

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    roles: List[Role]

class UpdateUserRequest(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    roles: Optional[List[Role]]