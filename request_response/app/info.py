from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from typing import Optional

info  = APIRouter()

class UserInfoIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    name: Optional[str] = None

class UserInfoOut(BaseModel):
    username: str
    email: EmailStr
    name: Optional[str] = None

@info.post('/user_info', response_model=UserInfoOut)
def create_user_info(user_info: UserInfoIn):
    return user_info

class ProductInfo(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: float = 10.5
    tags: list[str] = []

products = {
    'foo': {'name': 'Foo', 'price': 50.2},
    'bar': {'name': 'Bar', 'description': 'The Bartenders', 'price': 62, 'tax': 20.2}, 
    'baz': {'name': 'Baz', 'description': None, 'price': 50.2, 'tax': 10.5, 'tags': []}
}

@info.get('/read_products/{product_id}', response_model=ProductInfo, response_model_exclude_unset=True)
def read_product(product_id: str):
    return products[product_id]

@info.get('/read_exclude_products/{product_id}', response_model=ProductInfo, response_model_exclude={'description'})
def read_exclude_products(product_id: str):
    return products[product_id]