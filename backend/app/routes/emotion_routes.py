from fastapi import APIRouter
from app.schemas.emotion import (
    EmotionAnalyzeRequest,
    EmotionAnalyzeResponse,
)

router = APIRouter()


@router.post("/analyze", response_model=EmotionAnalyzeResponse)
def analyze_emotion(payload: EmotionAnalyzeRequest):
    """
    Analyzes emotion from text input.
    """
    return {
        "emotion": "neutral",
        "confidence": 0.0,
        "risk_level": "low",
    }
