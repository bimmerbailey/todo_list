from fastapi import status, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import schemas
from app.db.init_db import get_db
from app.crud import users
from typing import List

router = APIRouter(
    prefix="/api_v1/users",
    tags=['Users']
)


@router.get('', response_model=List[schemas.users.UserOut])
def get_users(db: Session = Depends(get_db)):
    return users.get_users(db=db)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=schemas.users.UserOut)
def create_user(user: schemas.users.UserCreate, db: Session = Depends(get_db)):
    return users.create_user(db=db, user=user)


@router.get('/{user_id}', response_model=schemas.users.UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return users.get_user(user_id=user_id, db=db)
