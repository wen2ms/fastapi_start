from pydantic import BaseModel, Field, field_validator
from datetime import date
from fastapi import APIRouter
from typing import Optional

data = APIRouter()

class Address(BaseModel):
    province: str
    city: str

class User(BaseModel):
    name: str = 'Root'
    age: int = Field(default=9, gt=6, lt=20)
    birth: Optional[date] = None
    friends_ages: list[int] = []
    address: Address

    @field_validator('name')
    def name_must_capital(cls, value):
        assert value.istitle(), 'Name must start with a capital letter'
        return value

@data.post('/data')
async def get_data(users: list[User]):
    return users