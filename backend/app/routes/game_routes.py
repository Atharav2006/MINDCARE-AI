from fastapi import APIRouter
from app.schemas.game import GameRecommendationResponse

router = APIRouter()


@router.get("/recommend", response_model=GameRecommendationResponse)
def recommend_games():
    """
    Returns recommended games based on emotional state.
    """
    return {
        "games": [
            {
                "id": "breathing_bubble",
                "name": "Breathing Bubble",
                "category": "anxiety",
            }
        ]
    }
