from pydantic import BaseModel


class EmotionAnalyzeRequest(BaseModel):
    text: str


class EmotionAnalyzeResponse(BaseModel):
    emotion: str
    confidence: float
    risk_level: str
