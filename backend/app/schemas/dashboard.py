from pydantic import BaseModel
from typing import List


class DashboardSummaryResponse(BaseModel):
    current_emotion: str
    weekly_trend: List[str]
    risk_score: int
