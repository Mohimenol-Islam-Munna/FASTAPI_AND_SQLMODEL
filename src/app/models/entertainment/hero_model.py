from sqlmodel import SQLModel, Field, Relationship
from typing import TypeVar
from .movie_model import MovieModel

class HeroModel(SQLModel, table=True):
    # fields 
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int = Field(default=None, ge=10)
    movie_id: int | None = Field(default=None, foreign_key="movie.id")
    movie: MovieModel | None = Relationship(back_populates="heros")
