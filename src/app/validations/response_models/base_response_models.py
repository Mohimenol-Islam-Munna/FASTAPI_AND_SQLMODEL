from pydantic import BaseModel

class BaseResponseModel(BaseModel):
    status: str | int
    message: str