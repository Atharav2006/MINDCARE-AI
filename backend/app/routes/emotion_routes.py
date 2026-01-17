from fastapi import APIRouter

router = APIRouter()


@router.post("/analyze")
def analyze_emotion(payload: dict):
    """
    Analyzes emotion from text input.
    """
    return {
        "emotion": "neutral",
        "confidence": 0.0,
        "risk_level": "low",
    }
