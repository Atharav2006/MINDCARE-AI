from app.models.user_state import UserState
from app.utils.logger import get_logger

logger = get_logger(__name__)

CRISIS_MESSAGE = (
    "I'm really sorry you're feeling this way. "
    "You’re not alone. Please reach out for immediate help."
)


def handle_crisis(user_state: UserState) -> dict:
    if user_state.risk_level == "critical":
        logger.warning(f"CRISIS detected for user {user_state.user_id}")

        return {
            "action": "crisis_support",
            "message": CRISIS_MESSAGE,
            "resources": [
                {"name": "Suicide & Crisis Lifeline", "contact": "988"},
                {"name": "Emergency Services", "contact": "Local emergency number"},
            ],
        }

    return {"action": "none"}
