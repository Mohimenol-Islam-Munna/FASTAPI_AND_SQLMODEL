from fastapi import FastAPI
from database import create_db_and_tables
from models import Hero
from database import engine
from sqlmodel import Session, select

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()



@app.get("/")
def home_route():

    hero_1 = Hero(name="Mahendra Sing Dhoni", secret_name="MSD")

    with Session(engine) as session:
        session.add(hero_1)

    return "this is home route"



@app.get('/another-route')
def another_route():
    return {
        "status": 200,
        "message": "Successful",
        "body": "This is another response"
    }


@app.get("/heros")
def heroList():

    allHero = select(Hero)

    print(allHero)

    return ""