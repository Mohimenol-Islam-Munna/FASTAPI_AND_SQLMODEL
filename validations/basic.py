from enum import Enum
from pydantic import BaseModel, Field


class PythonEnum(str, Enum):
    messi = "messi"
    lamin = "lamin"
    pedri = "pedri"


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


class PydanticModelValidation(BaseModel):
    name: str
    age: int | None = Field(default=None, title="Provide Valid age", ge=18)
    address: str | None = Field(default=None, min_length=5, max_length=20)
    contact: int = Field(default=0)


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
                    "contact": 12345678,
                }
            ]
        }
    }


class ResponseTypeModel(BaseModel):
    name: str
    age: int | None = Field(default=None, title="Provide Valid age", ge=18)
    address: str | None = Field(default=None, min_length=5, max_length=200)
    contact: int = Field(default=0)
