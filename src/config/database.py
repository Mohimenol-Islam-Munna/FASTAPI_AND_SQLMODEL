from sqlmodel import SQLModel, create_engine, Session
from . import models

sqlite_file_name = "./sqlite_db.db"

sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

def create_database():
    SQLModel.metadata.create_all(engine)


def create_session():
    session = Session(engine)

    return session