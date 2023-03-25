from data.member_data import db, User
from uuid import UUID
from fastapi import FastAPI, HTTPException
from models import UpdateUserRequest

app = FastAPI()

# Root
@app.get("/")
async def root():
    return {"Hello": "NewJeans"}

# Get request for all members
@app.get("/members")
async def fetch_members():
    return db;

# Get request for a member
@app.get("/members/{user_id}")
async def fetch_a_member(user_id: UUID):
    for user in db:
        if user.id == user_id:
            result = user
            return result
    raise HTTPException(
        status_code = 404,
        detail = f"Sorry, member with id: {user_id} does not exist."
    )

# Post request to add a new member
@app.post("/members")
async def register_member(user: User):
    db.append(user)
    return {"id": user.id}

# Delete a member 
@app.delete("/members/{user_id}")
async def delete_member(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return "Member has been successfully deleted."
    raise HTTPException(
        status_code = 404,
        detail = f"Sorry, member with id: {user_id} does not exist."
    )

# Update a member
@app.put("/members/{user_id}")
async def update_member(user_update: UpdateUserRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return user
    raise HTTPException(
        status_code = 404,
        detail = f"Sorry, member with id: {user_id} does not exist."
    )  