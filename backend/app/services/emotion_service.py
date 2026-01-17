import sys
from pathlib import Path

# -------------------------
# Add ai-services to path
# -------------------------
BASE_DIR = Path(__file__).resolve().parents[3]
AI_DIR = BASE_DIR / "ai-services" / "emotion-analysis"
sys.path.append(str(AI_DIR))

from predict import predict_emotion  # noqa

from app.models.emotion_model import EmotionResult
from app.utils.logger import get_logger

logger = get_logger(__name__)


def analyze_emotion(text: str) -> EmotionResult:
    """
    Analyze user emotion using ML-based AI service.
    """

    logger.info("Analyzing emotion using AI model")

    # -------------------------
    # AI Prediction
    # -------------------------
    result = predict_emotion(text)

    # -------------------------
    # Safety override (CRITICAL)
    # -------------------------
    if result.get("risk_level") == "high" and result.get("emotion") in [
        "sadness",
        "depression",
        "grief",
    ]:
        explanation = "High emotional distress detected."
    else:
        explanation = "Emotion inferred using AI model."

    return EmotionResult(
        emotion=result["emotion"],
        confidence=result["confidence"],
        primary_emotion=result.get("primary_emotion"),
        mood_group=result.get("mood_group"),
        risk_level=result.get("risk_level"),
        confidence_label=result.get("confidence_label"),
        secondary_emotions=result.get("secondary_emotions"),
        explanation=explanation,
    )
