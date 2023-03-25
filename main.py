from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from models import Gender, Role, UpdateUserRequest, User

app = FastAPI()

db: List[User] = [
    User(
        # id = uuid4(),
        id = UUID("cfa50d92-8d44-4ab5-9a74-c1a219132fdc"),
        first_name = "Hanni",
        last_name = "Pham",
        gender = Gender.female,
        roles = [Role.leader, Role.member]
    ),
    User(
        # id = uuid4(),
        id = UUID("8db4f49e-77ea-414a-a94a-ce1dc493ef8a"),
        first_name = "Minji",
        last_name = "Kim",
        gender = Gender.female,
        roles = [Role.member]
    ),
     User(
        # id = uuid4(),
        id = UUID("0cd8016f-5d0f-46be-b9e8-d20214cadfbc"),
        first_name = "Danielle",
        last_name = "Marsh",
        gender = Gender.female,
        roles = [Role.member]
    ),
     User(
        # id = uuid4(),
        id = UUID("dba1abb4-3901-4d2b-8d9e-c0a1090d3e3b"),
        first_name = "Haerin",
        last_name = "Kang",
        gender = Gender.female,
        roles = [Role.member]
    ),
     User(
        # id = uuid4(),
        id = UUID("1f2aedaf-45e8-4f7c-83c8-cfa64110da69"),
        first_name = "Hyein",
        last_name = "Lee",
        gender = Gender.female,
        roles = [Role.member, Role.maknae]
    )
]

# Home 
@app.get("/")
async def root():
    return {"Hello": "NewJeans"}

# Get request for users
@app.get("/members")
async def fetch_members():
    return db;

# Get request for a user
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

# Post request to add a new user
@app.post("/members")
async def register_member(user: User):
    db.append(user)
    return {"id": user.id}

# Delete a user 
@app.delete("/members/{user_id}")
async def delete_member(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code = 404,
        detail = f"Sorry, member with id: {user_id} does not exist."
    )

# Update user
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