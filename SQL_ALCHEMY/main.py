from fastapi import FastAPI, Query, status
from enum import Enum
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()


class PythonEnum(str, Enum):
    messi = "messi"
    lamin = "lamin"
    pedri = "pedri"


@app.get("/home")
def home():
    return {"status": "success", "message": "This is home route"}


@app.get("/home/{home_id}")
async def path_param(home_id: int):
    print("this is path params :", home_id)

    return {"status": "success", "message": f"this is path parameter : {home_id}"}


@app.get("/enum/{enum_value}")
def python_enum(enum_value: str):
    if enum_value == PythonEnum.lamin:
        return {"status": "success", "message": f"You entered {enum_value} in the path params"}
    elif enum_value == PythonEnum.messi:
        return {"status": "success", "message": f"You entered {enum_value} in the path params"}
    elif enum_value == PythonEnum.pedri:
        return {"status": "success", "message": f"You entered {enum_value} in the path params"}
    else:
        return {
            "status": "success",
            "message": f"Your entered value {enum_value} is no valid. Please try with valid value"
        }


@app.get("/query-params/")
def query_params(last: int | None = None, limit: int = 0):
    return {
        "status": "success",
        "limit": limit,
        "last": last
    }


class RequestBody(BaseModel):
    name: str
    age: int
    address: str
    contract: int


class OptionalRequestBody(BaseModel):
    name: str
    age: int | None = None
    address: str | None = None
    contract: int


@app.post("/request-body")
def request_body(body: RequestBody):
    return {
        "status": "success",
        "message": "Request with body",
        "data": body
    }


@app.post("/optional-request-body")
def optional_request_body(body: OptionalRequestBody):

    body_dict = body.model_dump()

    body_dict["age"] = 120

    body_dict.update({"name": "munna"})

    return {
        "status": "success",
        "message": "Request with optional body",
        "data": body,
        "data_dict": body_dict,
    }


@app.get("/additional-validation-with-query-params")
async def additional_validation_with_query_params(address: Annotated[str | None, Query(max_length=10)] = None):

    return {
        "status": "success",
        "message": "Validation of request params with annotated",
        "address": address
    }


@app.get("/multiple-query-params-with-same-name")
async def multiple_query_params_with_same_name(address: Annotated[list[str | None], Query()] = None):

    return {
        "status": "success",
        "message": "Validation of request params with annotated",
        "address": address
    }


class PydanticModelValidation(BaseModel):
    name: str
    age: int | None = Field(default=None, title="Provide Valid age", ge=18)
    address: str | None = Field(default=None, min_length=5, max_length=20)
    contact: int = Field(default=0)


@app.post("/pydantic-model-validation")
async def pydantic_model_validation(address: PydanticModelValidation):

    return {
        "status": "success",
        "message": "Pydantic model validation",
        "address": address
    }


class Student(BaseModel):
    name: str = Field(max_length=50)
    roll: int = Field()
    session: str = Field(max_length=20)
    className: str = Field(max_length=15)


class Teacher(BaseModel):
    name: str = Field(max_length=50)
    id: int = Field()
    subject: str = Field(max_length=20)
    classTeacherOf: str = Field(max_length=15)


class School(BaseModel):
    name: str = Field(max_length=50)
    address: str = Field(max_length=100)

    student: Student
    teacher: Teacher


@app.post("/nested-pydantic-model")
async def nested_pydantic_model(body: School):

    return {
        "status": "success",
        "message": "Nested Pydantic model validation",
        "address": body
    }


class DeclareRequestExampleData(BaseModel):
    name: str
    age: int | None = None
    address: str
    contact: int | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "munna",
                    "age": 18,
                    "address": "Agargaon Dhaka",
                    "contact": 12345678
                }
            ]
        }
    }


@app.post("/declare-request-example-data")
async def declare_request_example_data(data: DeclareRequestExampleData):

    data_dict = data.model_dump()

    print("data dict :", data_dict)

    return {
        "status": "Success",
        "message": "Declare request example data",
        "data_dict": data_dict,
        "data": data,
    }


class ResponseTypeModel(BaseModel):
    name: str
    age: int | None = Field(default=None, title="Provide Valid age", ge=18)
    address: str | None = Field(default=None, min_length=5, max_length=200)
    contact: int = Field(default=0)


@app.post("/response-type", response_model=ResponseTypeModel)
async def response_type():

    data = {
        "name": "munna", "age": 330, "address": "Mymensingh, Bangladesh", "contact": 1988906494
    }

    return data


@app.get("/http-status-code", status_code=status.HTTP_200_OK)
async def http_status_code():
    return {
        "message": "Response with http status code",
        "data": {"name": "munna", "id": 160144}
    }





















































































