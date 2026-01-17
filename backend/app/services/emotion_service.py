from app.utils.text_cleaner import clean_text
from app.models.emotion_model import EmotionResult
from app.utils.logger import get_logger

# Import AI predictor
from ai_services.emotion_analysis.predict import predict_emotion

logger = get_logger(__name__)


def analyze_emotion(text: str) -> EmotionResult:
    """
    Main emotion analysis pipeline.
    Uses ML model via ai-services, not keyword rules.
    """

    cleaned_text = clean_text(text)
    logger.info("Sending text to AI emotion model")

    try:
        ai_result = predict_emotion(cleaned_text)
        """
        ai_result example:
        {
          "emotion": "self_doubt",
          "confidence": 0.82,
          "raw_scores": {...}
        }
        """

        emotion = ai_result.get("emotion", "neutral")
        confidence = float(ai_result.get("confidence", 0.5))

        explanation = _generate_explanation(emotion, confidence)

        return EmotionResult(
            emotion=emotion,
            confidence=confidence,
            explanation=explanation,
        )

    except Exception as e:
        logger.error(f"Emotion analysis failed: {e}")

        # Safe fallback
        return EmotionResult(
            emotion="neutral",
            confidence=0.5,
            explanation="Emotion could not be confidently determined.",
        )


def _generate_explanation(emotion: str, confidence: float) -> str:
    """
    Human-readable explanation for dashboard & chat UI
    """
    explanations = {
        "depression": "Patterns indicate emotional heaviness and withdrawal.",
        "anxiety": "Signs of worry, tension, or fear detected.",
        "stress": "Language reflects overload or pressure.",
        "self_doubt": "Expressions of low confidence or self-questioning.",
        "procrastination": "Avoidance and delay behaviors detected.",
        "grief": "Loss-related emotional signals detected.",
        "anger": "Frustration or irritation patterns detected.",
        "neutral": "No dominant emotional signals detected.",
    }

    base = explanations.get(emotion, "Emotional signals detected.")
    return f"{base} (confidence: {round(confidence, 2)})"
