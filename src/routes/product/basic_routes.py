from fastapi import FastAPI, Query, status, Form, File, UploadFile, APIRouter
from typing import Annotated
from ...app.validations.dtos import basic_dto

router = APIRouter(
    prefix="/basics",
    tags=["basics"],
    dependencies=[],
    responses={404: {"description": "Not Found"}},
)


@router.get("/home")
def home():
    return {"status": "success", "message": "This is home route"}


@router.get("/home/{home_id}")
async def path_param(home_id: int):
    print("this is path params :", home_id)

    return {"status": "success", "message": f"this is path parameter : {home_id}"}


@router.get("/enum/{enum_value}")
def python_enum(enum_value: str):
    if enum_value == basic_dto.PythonEnum.lamin:
        return {
            "status": "success",
            "message": f"You entered {enum_value} in the path params",
        }
    elif enum_value == basic_dto.PythonEnum.messi:
        return {
            "status": "success",
            "message": f"You entered {enum_value} in the path params",
        }
    elif enum_value == basic_dto.PythonEnum.pedri:
        return {
            "status": "success",
            "message": f"You entered {enum_value} in the path params",
        }
    else:
        return {
            "status": "success",
            "message": f"Your entered value {enum_value} is no valid. Please try with valid value",
        }


@router.get("/query-params/")
def query_params(last: int | None = None, limit: int = 0):
    return {"status": "success", "limit": limit, "last": last}


@router.post("/request-body")
def request_body(body: basic_dto.RequestBody):
    return {"status": "success", "message": "Request with body", "data": body}


@router.post("/optional-request-body")
def optional_request_body(body: basic_dto.OptionalRequestBody):

    body_dict = body.model_dump()

    body_dict["age"] = 120

    body_dict.update({"name": "munna"})

    return {
        "status": "success",
        "message": "Request with optional body",
        "data": body,
        "data_dict": body_dict,
    }


@router.get("/additional-validation-with-query-params")
async def additional_validation_with_query_params(
    address: Annotated[str | None, Query(max_length=10)] = None
):

    return {
        "status": "success",
        "message": "Validation of request params with annotated",
        "address": address,
    }


@router.get("/multiple-query-params-with-same-name")
async def multiple_query_params_with_same_name(
    address: Annotated[list[str | None], Query()] = None
):

    return {
        "status": "success",
        "message": "Validation of request params with annotated",
        "address": address,
    }


@router.post("/pydantic-model-validation")
async def pydantic_model_validation(address: basic_dto.PydanticModelValidation):

    return {
        "status": "success",
        "message": "Pydantic model validation",
        "address": address,
    }


@router.post("/nested-pydantic-model")
async def nested_pydantic_model(body: basic_dto.School):

    return {
        "status": "success",
        "message": "Nested Pydantic model validation",
        "address": body,
    }


@router.post("/declare-request-example-data")
async def declare_request_example_data(data: basic_dto.DeclareRequestExampleData):

    data_dict = data.model_dump()

    print("data dict :", data_dict)

    return {
        "status": "Success",
        "message": "Declare request example data",
        "data_dict": data_dict,
        "data": data,
    }


@router.post("/response-type", response_model=basic_dto.ResponseTypeModel)
async def response_type():

    data = {
        "name": "munna",
        "age": 330,
        "address": "Mymensingh, Bangladesh",
        "contact": 1988906494,
    }

    return data


@router.get("/http-status-code", status_code=status.HTTP_200_OK)
async def http_status_code():
    return {
        "message": "Response with http status code",
        "data": {"name": "munna", "id": 160144},
    }


@router.post("/form-data", status_code=status.HTTP_201_CREATED)
async def form_data(
    username: Annotated[str, Form(min_length=8)], password: Annotated[str | int, Form()]
):
    return {"username": username, "password": password}


@router.post("/upload-file_with_file")
async def upload_file(file: Annotated[bytes, File()]):
    return {
        "message": "file uploaded successfully",
        "user_name": "name",
        "file_length": len(file),
    }


@router.post("/upload-file_with_upload_file")
async def upload_file(name: Annotated[str, Form()], file: UploadFile):
    return {
        "message": "file uploaded successfully",
        "user_name": name,
        "file_name": file.filename,
        "file_size": file.size,
        "file": file,
    }


@router.post("/files/")
async def create_file(file: Annotated[bytes, File()], token: Annotated[str, Form()]):
    return {
        "file_size": len(file),
        "token": token,
    }
