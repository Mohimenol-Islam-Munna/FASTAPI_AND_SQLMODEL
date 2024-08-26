from fastapi import APIRouter, status, Path, Body
from typing import Annotated
from sqlmodel import Session, select
from pydantic import BaseModel

from ...app.models.entertainment.hero_model import Hero
from ...app.models.entertainment.movie_model import Movie
from ...app.validations.dtos.response_dtos.movie_response_dtos import MovieResponseModel
from ...config.database import ENGINE

router = APIRouter(
    prefix="/heros",
    tags=["hero"],
    dependencies=[],
)

session = Session(ENGINE)


@router.get("/info", status_code=status.HTTP_200_OK)
def info():
    return {
        "message": "hero info",
    }


class CreateHero(BaseModel):
    name: str
    secret_name: str
    age: int
    movie_id: int | None


@router.post("/create")
def crete_hero(body: Annotated[CreateHero, Body()]):
    hero = Hero(
        name=body.name,
        secret_name=body.secret_name,
        age=body.age,
        movie_id=body.movie_id,
    )

    with Session(ENGINE) as session:
        session.add(hero)
        session.commit()

    return {
        "status": status.HTTP_200_OK,
        "data": body,
        "message": "Hero created successfully!",
    }


@router.get("/", status_code=status.HTTP_200_OK)
def get_heros():
    query = select(Hero)

    results = session.exec(query).all()

    return {"message": "hero retrieved successfully!", "data": results}


@router.put("/update/{hero_id}/{movie_id}", status_code=status.HTTP_200_OK)
def updateHero(hero_id: Annotated[int, Path()], movie_id: Annotated[int, Path()]):
    query = select(Hero).where(Hero.id == hero_id)

    hero = session.exec(query).first()

    hero.movie_id = movie_id

    session.commit()

    session.refresh(hero)

    return {"data": hero, "success": "Hero updated successfully"}


@router.get("/get-by-name/{name}", status_code=status.HTTP_200_OK)
def getHeroByName(name: Annotated[str, Path()]):
    query = select(Hero).where(Hero.name == name)

    result = session.exec(query).all()

    return {"data": result, "message": "success"}


@router.get("/id/{hero_id}", status_code=status.HTTP_200_OK)
def getHeroById(hero_id: Annotated[int, Path()]):
    query = select(Hero).where(Hero.id == hero_id)

    result = session.exec(query).first()

    return {"data": result, "message": "Data retrieved successfully"}


@router.get("/movies", status_code=status.HTTP_200_OK)
def getMovies():
    query = select(Movie)

    result = session.exec(query).all()

    return {"data": result, "message": "Data retrieved successfully!"}


class CreateMovie(BaseModel):
    name: str
    rating: float
    director: str


@router.post("/movies", status_code=status.HTTP_201_CREATED)
def createMovies(body: Annotated[CreateMovie, Body()]):

    query = Movie(name=body.name, rating=body.rating, director=body.director)

    with Session(ENGINE) as session:
        session.add(query)
        session.commit()

    return {
        "status": status.HTTP_200_OK,
        "data": body,
        "message": "movie created successfully!",
    }


@router.get(
    "/movies/{id}",
    response_model=MovieResponseModel,
    status_code=status.HTTP_200_OK,
)
async def movie_by_id(id: Annotated[int, Path()]):
    query = select(Movie).where(Movie.id == id)

    result = session.exec(query).one()

    return {
        "status": "success",
        "message": "Data retrieved successfully",
        "data": result,
    }


@router.get("/heros-with-movies", status_code=status.HTTP_200_OK)
def getHeroesWithMovies():
    query = select(Hero, Movie).where(Hero.id == Movie.id)

    results = session.exec(query)

    for result in results:
        print("$$$$$$$$$ result:", result)

    return {"data": "results", "message": "Data retrieved successfully!"}


@router.get("/heros-and-movies-join", status_code=status.HTTP_200_OK)
def getHeroesWithMovies():
    query = select(Movie, Hero).join(Movie)

    results = session.exec(query)

    for result in results:
        print("$$$$$$$$$ result:", result)

    return {"data": "results", "message": "Data retrieved successfully!"}


@router.get("/heros-and-movies-left-join", status_code=status.HTTP_200_OK)
def getHeroesAndMoviesLeftJoin():
    query = select(Hero, Movie).join(Movie, isouter=True)

    results = session.exec(query)

    for result in results:
        print("$$$$$$$$$ result:", result)

    return {"data": "results", "message": "Data retrieved successfully!"}


@router.get("/heros-and-movies-right-join", status_code=status.HTTP_200_OK)
def getHeroesAndMoviesRightJoin():
    query = select(Movie, Hero).join(Movie, isouter=True)

    results = session.exec(query).all()

    for result in results:
        print("$$$$$$$$$ result::", result)

    return {"data": "results", "message": "Data retrieved successfully!"}
