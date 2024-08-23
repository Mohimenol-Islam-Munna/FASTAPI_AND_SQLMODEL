from sqlmodel import SQLModel, Field, Relationship, Relationship


class Movie(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str 
    rating: float | None = Field(default=None, le=10.0)
    director: str | None = Field(default=None)
    heros: list['Hero'] | None = Relationship(back_populates="movie")

    def resolve_hero(self):
        # This method can be used if you need to work with the Hero class
        from .hero_model import Hero
        return Hero



