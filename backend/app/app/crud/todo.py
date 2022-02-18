from fastapi import status, HTTPException, Depends, Response
from sqlalchemy.orm import Session
from app import models, schemas
from sqlalchemy.orm import Session
from typing import List


def check_todo(todo_id, db, user_id):
    todo_query = db.query(models.todo.ToDo).filter(models.todo.ToDo.id == todo_id)

    if todo_query.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Post with id: {todo_id} does not exist')

    if todo_query.first().owner_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f'Not Authorized to do action')

    return todo_query


def get_todos(db: Session):
    return db.query(models.todo.ToDo).all()


def create_todo(db: Session, request: schemas.todo.ToDoBase, user_id):
    db_todo = models.todo.ToDo(description=request.description, owner_id=user_id)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def get_single_todo(todo_id: int, db: Session):
    todo_query = db.query(models.todo.ToDo).filter(models.todo.ToDo.id == todo_id).first()
    if not todo_query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id: {todo_id} does not exist')
    return todo_query


def delete_todo(todo_id: int, db: Session, user_id):
    todo_query = check_todo(todo_id=todo_id, db=db, user_id=user_id)
    todo_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


def update_todo(todo_id: int, todo: schemas.todo.ToDoBase, db: Session, user_id):
    todo_query = check_todo(todo_id=todo_id, db=db, user_id=user_id)
    todo_query.update(todo.dict(), synchronize_session=False)
    db.commit()

    return todo_query.first()
