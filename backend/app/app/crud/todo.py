from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from app import models, schemas
from sqlalchemy.orm import Session
from typing import List


def get_todos(db: Session):
    return db.query(models.todo.ToDo).all()


def create_todo(db: Session, request: schemas.todo.ToDo, user_id):
    db_todo = models.todo.ToDo(description=request.description, owner_id=user_id)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def get_single_todo(post_id: int, db: Session):
    post = db.query(models.todo.ToDo).filter(models.todo.ToDo.id == post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id: {post_id} does not exist')
    return post
