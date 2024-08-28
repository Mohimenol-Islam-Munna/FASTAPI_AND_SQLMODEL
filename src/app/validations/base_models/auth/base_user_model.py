from sqlmodel import SQLModel, Field

class BaseUserModel(SQLModel):
    username: str = Field()
    email: str = Field()
    full_name: str | None = Field(default=None)
    disabled: bool | None = Field(default=None)
