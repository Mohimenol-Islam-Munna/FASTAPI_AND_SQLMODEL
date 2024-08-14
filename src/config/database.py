from sqlmodel import SQLModel, create_engine
from schemas import Hero

sqlite_file_name = "./sqlite_db.db"

print("sqlite_file_name", sqlite_file_name)

sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)