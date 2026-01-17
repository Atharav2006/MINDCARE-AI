from pydantic import BaseModel
from typing import Optional


class ChatMessageRequest(BaseModel):
    message: str
    user_id: Optional[str] = None


class ChatMessageResponse(BaseModel):
    reply: str
    emotion: str
    confidence: float
