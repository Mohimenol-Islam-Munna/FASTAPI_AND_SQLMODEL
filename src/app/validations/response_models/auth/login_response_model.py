from pydantic import BaseModel, Field
from ..base_response_models import BaseResponseModel

class UserDataModel(BaseModel):
    id: int | None = Field(default=None)
    username: str = Field()
    email: str = Field()
    full_name: str | None = Field(default=None)
    disabled: bool = Field(default=False)

class LoginSuccessModel(BaseResponseModel):
    data: UserDataModel | None