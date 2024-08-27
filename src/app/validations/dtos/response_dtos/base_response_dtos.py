from pydantic import BaseModel

class BaseResponseModel(BaseModel):
    status: str
    message: str