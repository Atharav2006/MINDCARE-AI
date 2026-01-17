from datetime import datetime

from app.models.emotion_model import EmotionResult
from app.models.user_state import UserState, UserEmotionSnapshot


def evaluate_user_state(
    user_id: str,
    emotion_result: EmotionResult,
    history: list[UserEmotionSnapshot] | None = None
) -> UserState:
    emotion = emotion_result.emotion
    confidence = emotion_result.confidence

    if emotion in ["suicidal", "self_harm"] and confidence > 0.7:
        risk = "critical"
    elif emotion in ["depression", "anxiety", "stress"] and confidence > 0.6:
        risk = "high"
    elif emotion in ["sad", "fear"]:
        risk = "medium"
    else:
        risk = "low"

    snapshot = UserEmotionSnapshot(
        emotion=emotion,
        confidence=confidence,
        timestamp=datetime.utcnow(),
    )

    updated_history = history or []
    updated_history.append(snapshot)

    return UserState(
        user_id=user_id,
        current_emotion=emotion,
        risk_level=risk,
        history=updated_history,
    )
