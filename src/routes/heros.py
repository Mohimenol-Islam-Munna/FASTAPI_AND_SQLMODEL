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
    hero = Hero(name="ifti", secret_name="m13", age=28)

    with Session(engine) as session:
        session.add(hero)
        session.commit()

    return {"status": status.HTTP_200_OK, "message": "hero created successfully!"}


@router.get("/", status_code=status.HTTP_200_OK)
def get_heros():
    query = select(Hero)

    session = Session(engine)

    results = session.exec(query).all()

    print("results :", results)

    return {"message": "hero retrieved successfully!", "data": results}


@router.get("/{name}", status_code=status.HTTP_200_OK)
def getHeroByName(name: Annotated[str, Path()]):
    query = select(Hero).where(Hero.name == name)

    session = Session(engine)

    result = session.exec(query).all()

    return {"data": result, "message": "success"}


@router.get("/id/{hero_id}", status_code=status.HTTP_200_OK)
def getHeroById(hero_id: Annotated[int, Path()]):
    query = select(Hero).where(Hero.id == hero_id)

    session = Session(engine)

    result = session.exec(query).first()

    return {"data": result, "message": "Data retrieved successfully"}


@router.get("/movies", status_code=status.HTTP_200_OK)
def getMovies():
    query = select(Movie)

    session = Session(engine)

    result = session.exec(query).all()

    return {"data": result, "message": "Data retrieved successfully!"}


@router.post("/movies", status_code=status.HTTP_201_CREATED)
def getMovies():
    query = Movie("Premam", 8.0, "Best Director")

    with Session(engine) as session:
        session.add(query)
        session.commit()

    return {"status": status.HTTP_200_OK, "message": "movie created successfully!"}
