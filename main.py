from typing import List
from uuid import uuid4
from fastapi import FastAPI
from models import Gender, Role, User

app = FastAPI()

db: List[User] = [
    User(
        id = uuid4(),
        first_name = "Khoa",
        last_name = "Nguyen",
        gender = Gender.male,
        roles = [Role.student]
    ),
    User(
        id = uuid4(),
        first_name = "Jennifer",
        last_name = "Tran",
        gender = Gender.female,
        roles = [Role.admin, Role.user]
    )
]

@app.get("/")
async def root():
    return {"Hello": "Khoa"}

@app.get("/users")
async def fetch_users():
    return db;