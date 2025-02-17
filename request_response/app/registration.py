from fastapi import APIRouter, Form

registraion = APIRouter()

@registraion.post('/register')
async def register(username: str = Form(), password: str = Form()):
    return {"username": username, "password": password}