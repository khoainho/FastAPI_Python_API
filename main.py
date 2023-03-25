from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
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

# Home 
@app.get("/")
async def root():
    return {"Hello": "Khoa"}

# Get request for users
@app.get("/users")
async def fetch_users():
    return db;

# Post request to add a new user
@app.post("/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

# Delete a user 
@app.delete("/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code = 404,
        detail = f"Sorry, user with id: {user_id} does not exsits"
    )