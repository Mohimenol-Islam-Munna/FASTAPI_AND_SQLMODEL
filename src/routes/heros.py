from fastapi import APIRouter, status, Path
from typing import Annotated
from sqlmodel import Session, select
from ..schemas.hero import Hero
from ..schemas.movie import Movie
from ..config.database import engine

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


@router.post("/create")
def crete_hero():
    hero = Hero(name="Fahad Fasil", secret_name="FF", age=35)

    with Session(engine) as session:
        session.add(hero)
        session.commit()

    return {"status": status.HTTP_200_OK, "message": "hero created successfully!"}


@router.get("/", status_code=status.HTTP_200_OK)
def get_heros():
    query = select(Hero)

    results = session.exec(query).all()

    print("results :", results)

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


@router.post("/movies", status_code=status.HTTP_201_CREATED)
def getMovies():
    query = Movie(name="Drishyam 2", rating=10, director="Mohon Lal")

    with Session(engine) as session:
        session.add(query)
        session.commit()

    return {"status": status.HTTP_200_OK, "message": "movie created successfully!"}


@router.get("/heros-with-movies", status_code=status.HTTP_200_OK)
def getHeroesWithMovies():
    query = select(Hero, Movie).where(Hero.id == Movie.id)

    results = session.exec(query)

    for result in results:
        print("$$$$$$$$$ result:", result)

    return {"data": "results", "message": "Data retrieved successfully!"}


@router.get("/heros-and-movies-join", status_code=status.HTTP_200_OK)
def getHeroesWithMovies():
    query = select(Hero, Movie).join(Movie)

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
    query = select(Hero, Movie).join(Movie, isouter=True)

    results = session.exec(query).all()

    for result in results:
        print("$$$$$$$$$ result::", result)

    return {"data": "results", "message": "Data retrieved successfully!"}
