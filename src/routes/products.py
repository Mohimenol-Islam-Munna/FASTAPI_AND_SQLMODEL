from fastapi import APIRouter, status
from sqlmodel import Session
from ..schemas.product import Product
from ..config.database import engine

router = APIRouter(prefix="/product", tags=["products"], dependencies=[])


session = Session(engine)


@router.get("/info", status_code=status.HTTP_200_OK)
def info():
    return {"message": "This is the product route"}


@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_product():
    product = Product(title="Blue Shirt", price=500)

    session.add(product)

    session.commit()

    session.close()

    return {"status": status.HTTP_200_OK, "message": "product created successfully!"}

