from pydantic import BaseModel
from typing import List


class Game(BaseModel):
    id: str
    name: str
    category: str


class GameRecommendationResponse(BaseModel):
    games: List[Game]
