from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI
from models import Gender, Role, User

app = FastAPI()

db: List[User] = [
    User(
        # id = uuid4(),
        id = UUID("f4b20df0-1099-435a-a46c-79d083cb5b0d"),
        first_name = "Khoa",
        last_name = "Nguyen",
        gender = Gender.male,
        roles = [Role.student]
    ),
    User(
        # id = uuid4(),
        id = UUID("8db4f49e-77ea-414a-a94a-ce1dc493ef8a"),
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