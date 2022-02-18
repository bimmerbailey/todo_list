from pydantic import BaseModel
from datetime import datetime
from .users import UserOut


class ToDoBase(BaseModel):
    description: str


class ToDO(ToDoBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True
