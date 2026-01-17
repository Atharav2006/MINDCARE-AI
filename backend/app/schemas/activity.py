from pydantic import BaseModel
from typing import List


class Activity(BaseModel):
    id: str
    title: str
    duration_minutes: int


class ActivityRecommendationResponse(BaseModel):
    activities: List[Activity]
