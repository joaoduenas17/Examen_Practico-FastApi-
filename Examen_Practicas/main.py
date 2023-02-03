# pylint: disable=E0611,E0401
from typing import List

from fastapi import FastAPI, HTTPException
from models import User_Pydantic, UserIn_Pydantic, Users
from pydantic import BaseModel

from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise

app = FastAPI(title="Practical exam")


class Status(BaseModel):
    message: str


@app.get("/users", response_model=List[User_Pydantic])
async def get_users():
    return await User_Pydantic.from_queryset(Users.all())


@app.post("/users", response_model=User_Pydantic)
async def create_user(user: UserIn_Pydantic):
    user_obj = await Users.create(**user.dict(exclude_unset=True))
    return await User_Pydantic.from_tortoise_orm(user_obj)


register_tortoise(
    app,
    db_url="postgres://postgres:admin@localhost:5432/exam_BJ",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
