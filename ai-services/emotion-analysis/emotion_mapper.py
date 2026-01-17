"""
emotion_mapper.py

Purpose:
- Normalize raw ML model emotions
- Support blended emotions (Plutchik wheel)
- Assign mood group & risk level
- Produce backend + dashboard ready output
"""

# =====================================================
# 1. PRIMARY EMOTION NORMALIZATION (Plutchik)
# =====================================================

PRIMARY_EMOTION_MAP = {
    # JOY axis
    "ecstasy": "joy",
    "joy": "joy",
    "serenity": "joy",
    "optimism": "joy",

    # TRUST axis
    "admiration": "trust",
    "trust": "trust",
    "acceptance": "trust",
    "love": "trust",

    # FEAR axis
    "terror": "fear",
    "fear": "fear",
    "apprehension": "fear",
    "submission": "fear",

    # SURPRISE axis
    "amazement": "surprise",
    "surprise": "surprise",
    "distraction": "surprise",
    "awe": "surprise",

    # SADNESS axis
    "grief": "sadness",
    "sadness": "sadness",
    "pensiveness": "sadness",
    "disappointment": "sadness",
    "remorse": "sadness",

    # DISGUST axis
    "loathing": "disgust",
    "disgust": "disgust",
    "boredom": "disgust",
    "contempt": "disgust",

    # ANGER axis
    "rage": "anger",
    "anger": "anger",
    "annoyance": "anger",
    "aggressiveness": "anger",

    # ANTICIPATION axis
    "vigilance": "anticipation",
    "anticipation": "anticipation",
    "interest": "anticipation",
}

# =====================================================
# 2. MOOD GROUPS (UX / GAMES / ACTIVITIES)
# =====================================================

MOOD_GROUP_MAP = {
    "joy": "positive",
    "trust": "positive",

    "anticipation": "neutral",
    "surprise": "neutral",

    "fear": "negative",
    "sadness": "negative",
    "anger": "negative",
    "disgust": "negative",

    "neutral": "neutral"
}

# =====================================================
# 3. RISK LEVELS (MENTAL HEALTH SAFETY)
# =====================================================

RISK_LEVEL_MAP = {
    "joy": "low",
    "trust": "low",

    "anticipation": "low",
    "surprise": "low",

    "fear": "medium",
    "anger": "medium",
    "disgust": "medium",

    "sadness": "high",

    "neutral": "low"
}

# =====================================================
# 4. CONFIDENCE THRESHOLDS
# =====================================================

CONFIDENCE_THRESHOLDS = {
    "very_low": 0.30,
    "low": 0.45,
    "medium": 0.65,
    "high": 0.80
}

# =====================================================
# 5. BLENDED EMOTION COMBINATIONS (Plutchik)
# =====================================================

BLENDED_EMOTIONS = {
    frozenset(["joy", "anticipation"]): "optimism",
    frozenset(["joy", "trust"]): "love",
    frozenset(["trust", "fear"]): "submission",
    frozenset(["fear", "surprise"]): "awe",
    frozenset(["surprise", "sadness"]): "disappointment",
    frozenset(["sadness", "disgust"]): "remorse",
    frozenset(["disgust", "anger"]): "contempt",
    frozenset(["anger", "anticipation"]): "aggressiveness",
}

# =====================================================
# 6. CONFIDENCE LABELING
# =====================================================

def confidence_label(confidence: float) -> str:
    if confidence < CONFIDENCE_THRESHOLDS["very_low"]:
        return "very_low"
    if confidence < CONFIDENCE_THRESHOLDS["low"]:
        return "low"
    if confidence < CONFIDENCE_THRESHOLDS["medium"]:
        return "medium"
    return "high"


# =====================================================
# 7. MAIN MAPPING FUNCTION (UPDATED)
# =====================================================

def map_emotion(
    dominant_emotion: str,
    confidence: float,
    secondary_emotions: list | None = None
) -> dict:
    """
    Maps ML predictions into structured emotional insight.
    """

    dominant_emotion = dominant_emotion.lower().strip()
    secondary_emotions = secondary_emotions or []

    # Normalize dominant emotion
    primary = PRIMARY_EMOTION_MAP.get(dominant_emotion, "neutral")

    # Normalize secondary emotions
    secondary_primary = [
        PRIMARY_EMOTION_MAP.get(e["emotion"], "neutral")
        for e in secondary_emotions
    ]

    # Detect blended emotion
    blended = None
    if secondary_primary:
        pair = frozenset([primary, secondary_primary[0]])
        blended = BLENDED_EMOTIONS.get(pair)

    final_emotion = blended if blended else primary

    # Safety downgrade
    if confidence < 0.35:
        final_emotion = "neutral"
        primary = "neutral"

    mood_group = MOOD_GROUP_MAP.get(primary, "neutral")
    risk_level = RISK_LEVEL_MAP.get(primary, "low")

    return {
        "emotion": final_emotion,
        "primary_emotion": primary,
        "mood_group": mood_group,
        "risk_level": risk_level,
        "confidence": round(confidence, 3),
        "confidence_label": confidence_label(confidence),
        "secondary_emotions": secondary_emotions,
    }


# =====================================================
# 8. LOCAL TEST
# =====================================================

if __name__ == "__main__":
    test_cases = [
        ("grief", 0.82, [{"emotion": "boredom", "confidence": 0.51}]),
        ("fear", 0.71, [{"emotion": "surprise", "confidence": 0.46}]),
        ("joy", 0.77, [{"emotion": "anticipation", "confidence": 0.49}]),
        ("anger", 0.68, [{"emotion": "anticipation", "confidence": 0.44}]),
        ("amazement", 0.55, [{"emotion": "sadness", "confidence": 0.41}]),
        ("remorse", 0.32, [{"emotion": "disgust", "confidence": 0.29}]),
    ]

    for emo, conf, sec in test_cases:
        print(map_emotion(emo, conf, sec))
