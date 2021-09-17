from fastapi import FastAPI
from app.db.init_db import engine

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
