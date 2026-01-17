from fastapi import APIRouter
from app.schemas.chat import ChatMessageRequest, ChatMessageResponse

router = APIRouter()


@router.post("/message", response_model=ChatMessageResponse)
def send_message(payload: ChatMessageRequest):
    return {
        "reply": "This is a placeholder response.",
        "emotion": "neutral",
        "confidence": 0.0,
    }
