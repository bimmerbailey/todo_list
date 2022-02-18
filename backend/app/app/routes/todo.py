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
async def all_todos(db: Session = Depends(get_db)):
    return crud.todo.get_todos(db)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=schemas.todo.ToDO)
async def create(request: schemas.todo.ToDoBase, db: Session = Depends(get_db), current_user=Depends(oauth.get_current_user)):
    return crud.todo.create_todo(db, request, current_user.id)


@router.get('/{todo_id}', response_model=schemas.todo.ToDO)
async def get_todo(todo_id, db: Session = Depends(get_db), current_user=Depends(oauth.get_current_user)):
    return crud.todo.get_single_todo(todo_id, db)


@router.delete('/{todo_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id, db: Session = Depends(get_db), current_user=Depends(oauth.get_current_user)):
    return crud.todo.delete_todo(todo_id, db, current_user.id)


@router.put('/{todo_id}', response_model=schemas.todo.ToDO)
async def update_todo(todo_id, todo_data: schemas.todo.ToDoBase, db: Session = Depends(get_db),
                      current_user=Depends(oauth.get_current_user)):
    return crud.todo.update_todo(todo_id=todo_id, db=db, todo=todo_data, user_id=current_user.id)
