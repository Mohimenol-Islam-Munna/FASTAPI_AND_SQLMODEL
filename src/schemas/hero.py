from sqlmodel import SQLModel, Field

class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int = Field(default=None, ge=10)
    movie_id: int | None = Field(default=None, foreign_key="movie.id")