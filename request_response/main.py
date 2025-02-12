from fastapi import FastAPI
import uvicorn
from app.user import user

app = FastAPI()

app.include_router(user, tags=['path parameters'])

if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)
