from fastapi import APIRouter

router = APIRouter()


@router.get("/summary")
def dashboard_summary():
    """
    Returns dashboard metrics and trends.
    """
    return {
        "current_emotion": "neutral",
        "weekly_trend": [],
        "risk_score": 0,
    }
