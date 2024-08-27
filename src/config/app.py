from fastapi import FastAPI
from typing import Final

from .globals import GLOBAL_DEPENDENCIES
from .routes import router


def bootstrap() -> FastAPI:
    # Create FastApi Instance
    app: Final[FastAPI] = FastAPI(dependencies=GLOBAL_DEPENDENCIES)

    # Register Routers
    app.include_router(router)

    return app
