from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from app.db.init_db import get_db
from app import crud, schemas

router = APIRouter(
    prefix="/api_v1/todo",
    tags=['ToDos']
)


@router.get('/')
def all_todos(db: Session = Depends(get_db)):
    return crud.todo.get_todos(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.todo.ToDo, db: Session = Depends(get_db)):
    return crud.todo.create_todo(db, request)
