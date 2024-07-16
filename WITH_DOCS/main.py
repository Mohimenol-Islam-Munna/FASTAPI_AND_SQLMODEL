import json
from enum import Enum
from fastapi import FastAPI, Query, Path
from pydantic import BaseModel, Field
from typing import Union, Annotated, ClassVar
from typing_extensions import Annotated

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
    print("path parameter function called")
    return {"message": "success", "id": id}


@app.get("/pre-defined-path-parameter/{path}")
def pre_defined_path_parameter(path: ModelName):
    return {"message": "success", "param": path}


# query parameter
@app.get("/query_params")
async def query_parameter(
    required_param: bool,
    start: int = 0,
    end: int = 10,
    is_active: bool = False,
):
    return {
        "message": "success",
        "isActive": is_active,
        "start": start,
        "end": end,
    }


# data modal
class Product(BaseModel):
    title: str
    stock: int
    price: float
    isActive: bool = True
    description: Union[str, None] = None


@app.post("/path-with-request-body")
def path_with_request_body(item: Product):
    return {"message": "Product created successfully!", "data": item}


# Query parameter and string validation
@app.get("/qp-and-string-validation")
def qp_and_string_validation(
    q: Annotated[Union[str, None], Query(max_length=10)] = None
):
    return {"message": "success", "param": q}


# default with ellipsis
@app.get("/default-with-ellipsis")
def default_with_ellipsis(q: Union[str, None] = ...):
    return {
        "message": "success",
        "param": q,
    }


# path parameter and numeric validation
@app.get("/path-parameter_and_number_validation/{id}")
def path_parameter_and_number_validation(id: Annotated[int, Path(ge=10)]):
    return {"message": "success", "id": id}



class StudentModel(BaseModel):
    id: int
    name: str = Field(alias="username")
    dept: Annotated[str | None, Field(default=None)]


class User(BaseModel):
    name: str = Field(repr=True)  
    age: int = Field(repr=False)




@app.get("/pydantic/{item}")
def pydantic_item_route(item: int | None):

    student = StudentModel(id=1, username = "munna")

    print("student :", student.dept)

    user = User(name='John', age=42)
    print(user)

    return {
        "status": 200,
        "message": f"Successfully validate",
        "student": student
    }
