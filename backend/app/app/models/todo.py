from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.init_db import Base


class ToDo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
