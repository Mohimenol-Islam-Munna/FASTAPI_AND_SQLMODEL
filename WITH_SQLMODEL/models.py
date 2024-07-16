from sqlmodel import SQLModel, Field

class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(default="")
    secret_name: str = Field(default="")
    age: int = Field(default=0)

