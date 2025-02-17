from fastapi import FastAPI
import uvicorn
from app.user import user
from app.job import job
from app.data import data
from app.registration import registraion

app = FastAPI()

app.include_router(user, tags=['path parameters'])
app.include_router(job, tags=['query parameters'])
app.include_router(data, tags=['request body'])
app.include_router(registraion, tags=['form data'])

if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)