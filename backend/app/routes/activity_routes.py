from fastapi import APIRouter

router = APIRouter()


@router.get("/recommend")
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
