from sqlalchemy.orm import DeclarativeBase 

print(dir(DeclarativeBase))


class Base(DeclarativeBase):
    pass