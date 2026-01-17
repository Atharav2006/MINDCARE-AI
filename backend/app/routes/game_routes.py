from fastapi import APIRouter

router = APIRouter()


@router.get("/recommend")
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
