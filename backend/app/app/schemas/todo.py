from typing import List, Optional
from pydantic import BaseModel


class ToDo(BaseModel):
    description: str
