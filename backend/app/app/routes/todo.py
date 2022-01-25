from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from app.db.init_db import get_db
from app import crud, schemas, oauth

router = APIRouter(
    prefix="/api_v1/todos",
    tags=['ToDos']
)


@router.get('')
def all_todos(db: Session = Depends(get_db)):
    return crud.todo.get_todos(db)


@router.post('', status_code=status.HTTP_201_CREATED)
def create(request: schemas.todo.ToDo, db: Session = Depends(get_db), current_user=Depends(oauth.get_current_user)):
    return crud.todo.create_todo(db, request, current_user.id)


@router.get('/{post_id}')
def get_todo(post_id, db: Session = Depends(get_db), current_user=Depends(oauth.get_current_user)):
    return crud.todo.get_single_todo(post_id, db)
