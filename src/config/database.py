from sqlmodel import SQLModel, create_engine, Session

SQLITE_FILE_NAME = "./sqlite_db.db"

SQLITE_URL = f"sqlite:///{SQLITE_FILE_NAME}"

ENGINE = create_engine(SQLITE_URL, echo=True)

def create_session():
    with Session(ENGINE) as session:
        yield session