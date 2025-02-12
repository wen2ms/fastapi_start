from fastapi import APIRouter

shop = APIRouter()

@shop.post('/books')
def shop_books():
    return {"shop": "books"}

@shop.post('/beds')
def shop_beds():
    return {"shop": "beds"}