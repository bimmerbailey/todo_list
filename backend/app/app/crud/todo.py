from sqlalchemy.orm import Session

# from app.models import todo as todo_models
# from app.schemas import todo as todo_schemas
from app import models, schemas


def get_todos(db: Session):
    return db.query(models.todo.ToDo).all()


def create_todo(db: Session, request: schemas.todo.ToDo):
    db_todo = models.todo.ToDo(description=request.description)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo
