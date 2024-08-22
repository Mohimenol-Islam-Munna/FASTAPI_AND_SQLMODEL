from fastapi import FastAPI
from .database import create_database
from .routes import router


def bootstrap(app: FastAPI):
    # Database Connection
    create_database()

    # Register Global Middlewares

    # Register Global Validations

    # Register Routers
    app.include_router(router)
