from fastapi import FastAPI, status
from typing import Annotated
from routes import basics
from config.database import engine, SQLModel

app = FastAPI()

SQLModel.metadata.create_all(engine)

app.include_router(basics.router)


@app.get("/")
def root():
    return {"status": status.HTTP_200_OK, "title": "This is the root."}
