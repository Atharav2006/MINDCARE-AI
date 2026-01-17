from pydantic import BaseModel
from typing import Optional


class EmotionResult(BaseModel):
    emotion: str
    confidence: float
    explanation: Optional[str] = None
