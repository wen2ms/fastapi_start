from fastapi import FastAPI
import uvicorn
from app.user import user
from app.job import job

app = FastAPI()

app.include_router(user, tags=['path parameters'])
app.include_router(job, tags=['query parameters'])

if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)