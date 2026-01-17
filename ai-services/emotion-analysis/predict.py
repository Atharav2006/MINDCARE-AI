import joblib
from pathlib import Path
from typing import Dict, List

from emotion_mapper import map_emotion

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "emotion_model.pkl"

model = joblib.load(MODEL_PATH)

CONFIDENCE_THRESHOLD = 0.35
TOP_K = 3


def predict_emotion(text: str) -> Dict:
    """
    Predict emotion using trained ML model.
    Returns dominant + secondary emotions.
    """

    probs = model.predict_proba([text])[0]
    classes = model.classes_

    # Pair emotions with probabilities
    emotion_scores = list(zip(classes, probs))

    # Sort by confidence
    emotion_scores.sort(key=lambda x: x[1], reverse=True)

    # Filter weak signals
    strong_emotions = [
        (emo, float(score))
        for emo, score in emotion_scores
        if score >= CONFIDENCE_THRESHOLD
    ]

    # Fallback
    if not strong_emotions:
        return {
            "emotion": "neutral",
            "confidence": 0.5,
            "secondary_emotions": [],
            "raw_scores": dict(emotion_scores),
        }

    # Dominant emotion
    dominant_emotion, dominant_confidence = strong_emotions[0]

    # Secondary emotions (blends)
    secondary = [
        {"emotion": emo, "confidence": round(score, 3)}
        for emo, score in strong_emotions[1:TOP_K]
    ]

    # Map via Plutchik / custom ontology
    mapped = map_emotion(
        dominant_emotion=dominant_emotion,
        confidence=dominant_confidence,
        secondary_emotions=secondary,
    )

    return {
        "emotion": mapped["emotion"],
        "confidence": round(mapped["confidence"], 3),
        "secondary_emotions": mapped.get("secondary_emotions", []),
        "raw_scores": {
            emo: round(score, 4) for emo, score in emotion_scores
        },
    }
