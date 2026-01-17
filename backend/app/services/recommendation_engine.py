def recommend_activity(emotion: str) -> dict:
    recommendations = {
        "anxiety": {
            "type": "breathing",
            "title": "Breathing Bubble",
            "duration": "5 min",
        },
        "stress": {
            "type": "game",
            "title": "Memory Light",
            "duration": "7 min",
        },
        "depression": {
            "type": "activity",
            "title": "Gratitude Match",
            "duration": "10 min",
        },
        "neutral": {
            "type": "focus",
            "title": "Focus Flow",
            "duration": "5 min",
        },
    }

    return recommendations.get(emotion, recommendations["neutral"])
