from typing import List
from uuid import UUID
from models import Gender, Role, User

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