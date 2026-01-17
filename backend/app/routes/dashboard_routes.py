from fastapi import APIRouter
from app.schemas.dashboard import DashboardSummaryResponse

router = APIRouter()


@router.get("/summary", response_model=DashboardSummaryResponse)
def dashboard_summary():
    """
    Returns dashboard metrics and trends.
    """
    return {
        "current_emotion": "neutral",
        "weekly_trend": [],
        "risk_score": 0,
    }
