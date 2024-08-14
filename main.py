from fastapi import FastAPI, Query, status, Form, File, UploadFile
from typing import Annotated
from routes import basics

app = FastAPI()

app.include_router(basics.router)


@app.get("/")
def root():
    return {"status": status.HTTP_200_OK, "title": "This is the root."}
