from fastapi import FastAPI
from .routes import router


def bootstrap(app: FastAPI):
    # Register Global Middlewares

    # Register Global Validations

    # Register Routers
    app.include_router(router)

