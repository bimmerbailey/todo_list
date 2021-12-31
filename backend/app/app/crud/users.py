from fastapi import status, HTTPException
from app import models, schemas
from sqlalchemy.orm import Session
from app import utils


def get_users(db: Session):
    return db.query(models.users.User).all()


def create_user(db: Session, user: schemas.users.UserCreate):
    # hash the password - user.password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.users.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_user(user_id: int, db: Session):
    user = db.query(models.users.User).filter(models.users.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {user_id} does not exist")

    return user

