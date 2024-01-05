from fastapi import FastAPI
from enum import Enum

# create  fastapi instance
app = FastAPI(debug=True)


# create enum class
class ModelName(str, Enum):
    messi = "messi"
    ronaldo = "ronaldo"
    mash = "mash"


@app.get("/")
def home():
    return "This is home route of our application"


# path parameter
@app.get("/path-parameter/me")
def path_parameter_order():
    return {"message": "success", "param": "me"}


@app.get("/path-parameter/{id}")
def path_parameter(id: int):
    print("path parameter function hitted")
    return {"message": "success", "id": id}


@app.get("/pre-defined-path-parameter/{path}")
def pre_defined_path_parameter(path: ModelName):
    return {"message": "success", "param": path}
