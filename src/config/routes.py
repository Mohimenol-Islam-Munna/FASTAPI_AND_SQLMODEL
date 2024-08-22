from fastapi import APIRouter

from ..routes.product import basic_routes

from ..routes.entertainment import hero_routes
from ..routes.product import product_routes

BASE_PATH = "/api/v1"

router = APIRouter(prefix=f"{BASE_PATH}")

router.include_router(basic_routes.router)

router.include_router(hero_routes.router)

router.include_router(product_routes.router)