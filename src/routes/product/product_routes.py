from fastapi import APIRouter, status
from sqlmodel import Session
from ...app.models.products.product_model import Product

from ...config.database import ENGINE

router = APIRouter(prefix="/products", tags=["products"], dependencies=[])


session = Session(ENGINE)


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

