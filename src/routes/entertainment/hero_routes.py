from fastapi import APIRouter, status, Path, Body
from typing import Annotated
from sqlmodel import Session, select
from pydantic import BaseModel

from ...app.models.entertainment.hero_model import HeroModel
from ...app.models.entertainment.movie_model import MovieModel
from ...config.database import engine

router = APIRouter(
    prefix="/heros",
    tags=["hero"],
    dependencies=[],
)

session = Session(engine)


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
    hero = HeroModel(
        name=body.name,
        secret_name=body.secret_name,
        age=body.age,
        movie_id=body.movie_id,
    )

    with Session(engine) as session:
        session.add(hero)
        session.commit()

    return {
        "status": status.HTTP_200_OK,
        "data": body,
        "message": "hero created successfully!",
    }


@router.get("/", status_code=status.HTTP_200_OK)
def get_heros():
    query = select(HeroModel)

    results = session.exec(query).all()

    print("results :", results)

    return {"message": "hero retrieved successfully!", "data": results}


@router.put("/update/{hero_id}/{movie_id}", status_code=status.HTTP_200_OK)
def updateHero(hero_id: Annotated[int, Path()], movie_id: Annotated[int, Path()]):
    query = select(HeroModel).where(HeroModel.id == hero_id)

    hero = session.exec(query).first()

    hero.movie_id = movie_id

    session.commit()

    session.refresh(hero)

    return {"data": hero, "success": "Hero updated successfully"}


@router.get("/get-by-name/{name}", status_code=status.HTTP_200_OK)
def getHeroByName(name: Annotated[str, Path()]):
    query = select(HeroModel).where(HeroModel.name == name)

    result = session.exec(query).all()

    return {"data": result, "message": "success"}


@router.get("/id/{hero_id}", status_code=status.HTTP_200_OK)
def getHeroById(hero_id: Annotated[int, Path()]):
    query = select(HeroModel).where(HeroModel.id == hero_id)

    result = session.exec(query).first()

    return {"data": result, "message": "Data retrieved successfully"}


@router.get("/movies", status_code=status.HTTP_200_OK)
def getMovies():
    query = select(MovieModel)

    result = session.exec(query).all()

    return {"data": result, "message": "Data retrieved successfully!"}


class CreateMovie(BaseModel):
    name: str
    rating: float
    director: str


@router.post("/movies", status_code=status.HTTP_201_CREATED)
def createMovies(body: Annotated[CreateMovie, Body()]):

    query = MovieModel(name=body.name, rating=body.rating, director=body.director)

    with Session(engine) as session:
        session.add(query)
        session.commit()

    return {
        "status": status.HTTP_200_OK,
        "data": body,
        "message": "movie created successfully!",
    }


@router.get("/heros-with-movies", status_code=status.HTTP_200_OK)
def getHeroesWithMovies():
    query = select(HeroModel, MovieModel).where(HeroModel.id == MovieModel.id)

    results = session.exec(query)

    for result in results:
        print("$$$$$$$$$ result:", result)

    return {"data": "results", "message": "Data retrieved successfully!"}


@router.get("/heros-and-movies-join", status_code=status.HTTP_200_OK)
def getHeroesWithMovies():
    query = select(MovieModel, HeroModel).join(MovieModel)

    results = session.exec(query)

    for result in results:
        print("$$$$$$$$$ result:", result)

    return {"data": "results", "message": "Data retrieved successfully!"}


@router.get("/heros-and-movies-left-join", status_code=status.HTTP_200_OK)
def getHeroesAndMoviesLeftJoin():
    query = select(HeroModel, MovieModel).join(MovieModel, isouter=True)

    results = session.exec(query)

    for result in results:
        print("$$$$$$$$$ result:", result)

    return {"data": "results", "message": "Data retrieved successfully!"}


@router.get("/heros-and-movies-right-join", status_code=status.HTTP_200_OK)
def getHeroesAndMoviesRightJoin():
    query = select(MovieModel, HeroModel).join(MovieModel, isouter=True)

    results = session.exec(query).all()

    for result in results:
        print("$$$$$$$$$ result::", result)

    return {"data": "results", "message": "Data retrieved successfully!"}
