from pydantic import BaseModel
from ....models.entertainment.hero_model import Hero
from .base_response_dtos import BaseResponseModel

class DataModel(BaseModel):
    id: int | None
    name: str
    rating: float | None
    director: str | None
    heros: list[Hero] | None


class MovieResponseModel(BaseResponseModel):
    data: DataModel
    