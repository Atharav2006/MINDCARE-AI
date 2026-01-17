from pydantic import BaseModel, Field
from typing import List
from datetime import datetime


class UserEmotionSnapshot(BaseModel):
    emotion: str
    confidence: float
    timestamp: datetime


class UserState(BaseModel):
    user_id: str
    current_emotion: str
    risk_level: str  # low | medium | high | critical
    history: List[UserEmotionSnapshot] = Field(default_factory=list)
