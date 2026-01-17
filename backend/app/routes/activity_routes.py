from fastapi import APIRouter
from app.schemas.activity import ActivityRecommendationResponse

router = APIRouter()


@router.get("/recommend", response_model=ActivityRecommendationResponse)
def recommend_activities():
    """
    Returns recommended mental health activities.
    """
    return {
        "activities": [
            {
                "id": "breathing",
                "title": "Breathing Exercise",
                "duration_minutes": 5,
            }
        ]
    }
