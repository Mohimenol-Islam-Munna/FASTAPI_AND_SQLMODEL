from fastapi import FastAPI, Request
from typing import Final

from .globals import GLOBAL_DEPENDENCIES
from .routes import router
from ..app.middlewares.auth_middleware import auth_middleware


def bootstrap() -> FastAPI:
    # Create FastApi Instance
    app: Final[FastAPI] = FastAPI(dependencies=GLOBAL_DEPENDENCIES)

    # Register Middlewares
    @app.middleware("http")
    async def http_middleware(request: Request, call_next):
        return await auth_middleware(request, call_next)

    # Register Routers
    app.include_router(router)

    return app
