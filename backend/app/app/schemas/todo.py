from pydantic import BaseModel


class ToDo(BaseModel):
    description: str
