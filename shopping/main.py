from fastapi import FastAPI
import uvicorn
from apps.shop.router import shop
from apps.user.router import user

app = FastAPI()

app.include_router(shop, prefix='/shop', tags=['Shop Interface'])
app.include_router(user, prefix='/user', tags=['User Interface'])

if __name__ == "__main__":
    uvicorn.run('main:app')