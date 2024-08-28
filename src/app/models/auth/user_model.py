from sqlmodel import Field

from ...validations.base_models.auth.base_user_model import BaseUserModel

class User(BaseUserModel, table=True):
    id: int | None = Field(default=None, primary_key=True)