from fastapi import FastAPI, status
from .routes import basics, heros, products
from .config.database import engine, SQLModel

app = FastAPI()

print("------------fast api app----------------- :", __name__)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


create_db_and_tables()


@app.get("/")
def root():
    return {"status": status.HTTP_200_OK, "title": "This is the root."}


app.include_router(basics.router)

app.include_router(heros.router)

app.include_router(products.router)
