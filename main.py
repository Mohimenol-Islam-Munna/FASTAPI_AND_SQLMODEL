from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    pyDict = {"id": 1, "name": "munna", "campus": "PUST", "subject": "CSE"}
    name = pyDict["name"]
    subject = pyDict.get("campus")
    pyDict["session"] = "2015-16"
    pyDict.pop("subject")
    pyDict.popitem()
    pyDict.clear()

    return pyDict


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}