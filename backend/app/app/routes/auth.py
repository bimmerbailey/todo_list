from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from app import models, utils
from app.db import init_db
from app.schemas import users
from app import oauth

router = APIRouter(tags=['Authentication'], prefix='/api_v1')


@router.post('/login', response_model=users.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(init_db.get_db)):
    user = db.query(models.users.User).filter(
        models.users.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    access_token = oauth.create_access_token(data={"user_id": user.id})

    return {"access_token": access_token, "token_type": "bearer"}


# TODO: update this. https://github.com/tiangolo/fastapi/issues/2263,
#  https://fastapi-users.github.io/fastapi-users/usage/routes/
@router.get("/logout")
async def route_logout_and_remove_cookie():
    response = RedirectResponse(url="/")
    response.delete_cookie("Authorization", domain="localhost")
    return response
