from sqlmodel import SQLModel, Field

class Movie(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str 
    rating: float | None = Field(default=None, le=10.0)
    director: int | None = Field(default=None)
    