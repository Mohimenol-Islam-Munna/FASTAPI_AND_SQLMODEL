from sqlmodel import SQLModel, create_engine
from ..schemas import hero, product, movie

sqlite_file_name = "./sqlite_db.db"

sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)