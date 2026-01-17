from pydantic import BaseModel
from typing import Optional, List, Dict


class EmotionResult(BaseModel):
    # Core (required)
    emotion: str                  # final emotion (possibly blended)
    confidence: float             # model confidence (0–1)

    # AI-enriched fields
    primary_emotion: Optional[str] = None
    mood_group: Optional[str] = None
    risk_level: Optional[str] = None
    confidence_label: Optional[str] = None

    # Advanced
    secondary_emotions: Optional[List[Dict]] = None

    # Human-readable explanation (optional)
    explanation: Optional[str] = None
