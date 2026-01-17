from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.config import settings
from app.routes import (
    chat_routes,
    emotion_routes,
    activity_routes,
    game_routes,
    dashboard_routes,
)
from app.utils.logger import setup_logging, get_logger

setup_logging()
logger = get_logger(__name__)


# -----------------------------
# App Initialization
# -----------------------------
app = FastAPI(
    title="MindCare-AI Backend",
    description="API layer for MindCare-AI mental health assistant",
    version="1.0.0",
)

# -----------------------------
# Middleware
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Routes Registration
# -----------------------------
app.include_router(chat_routes.router, prefix="/chat", tags=["Chat"])
app.include_router(emotion_routes.router, prefix="/emotion", tags=["Emotion"])
app.include_router(activity_routes.router, prefix="/activities", tags=["Activities"])
app.include_router(game_routes.router, prefix="/games", tags=["Games"])
app.include_router(dashboard_routes.router, prefix="/dashboard", tags=["Dashboard"])

# -----------------------------
# Health Check
# -----------------------------
@app.get("/health", tags=["System"])
def health_check():
    return {
        "status": "ok",
        "service": "MindCare-AI Backend",
        "environment": settings.ENVIRONMENT,
    }

# -----------------------------
# Global Exception Handler
# -----------------------------
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "message": "Something went wrong. Please try again later.",
        },
    )

