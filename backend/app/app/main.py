from fastapi import FastAPI
from app.db.init_db import engine
from app import models, crud, routes

app = FastAPI()

models.todo.Base.metadata.create_all(engine)

app.include_router(routes.todo.router)
