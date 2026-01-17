from app.utils.text_cleaner import clean_text
from app.models.emotion_model import EmotionResult
from app.utils.logger import get_logger

logger = get_logger(__name__)


def analyze_emotion(text: str) -> EmotionResult:
    cleaned = clean_text(text)
    logger.info(f"Analyzing emotion for text")

    if any(word in cleaned for word in ["suicide", "kill myself", "end it"]):
        return EmotionResult(
            emotion="suicidal",
            confidence=0.92,
            explanation="High-risk self-harm language detected.",
        )

    if any(word in cleaned for word in ["sad", "depressed", "hopeless"]):
        return EmotionResult(
            emotion="depression",
            confidence=0.88,
            explanation="Depressive language patterns detected.",
        )

    if any(word in cleaned for word in ["anxious", "panic", "nervous"]):
        return EmotionResult(
            emotion="anxiety",
            confidence=0.81,
            explanation="Anxiety indicators detected.",
        )

    return EmotionResult(
        emotion="neutral",
        confidence=0.65,
        explanation="No strong emotional signals detected.",
    )
