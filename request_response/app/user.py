from fastapi import APIRouter

user = APIRouter()

# Route matching is in order

# @user.get('/user/1')
# def get_user():
#     return {"user_id": "root"}

@user.get('/user/{user_id}')
def get_user(user_id: int):
    return {"user_id": user_id}

@user.get('/articles/{article_id}')
def get_article(article_id: int):
    return {"article_id": article_id}