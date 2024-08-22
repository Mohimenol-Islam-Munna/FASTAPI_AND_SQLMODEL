from sqlmodel import Field, SQLModel

class ProductModel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field()
    price: int = Field()