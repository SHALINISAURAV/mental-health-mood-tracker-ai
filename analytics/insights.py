def generate_behavioral_insight(common_emotion):

    insights = {
        "joy":
            "You generally seem emotionally positive 😊",

        "sadness":
            "Your recent journals indicate emotional stress 💙",

        "fear":
            "Anxiety or stress patterns are appearing ⚠️",

        "anger":
            "Frustration levels seem elevated 🔥",

        "love":
            "Your journals reflect emotional connection ❤️",

        "surprise":
            "Unexpected events may be affecting your mood 😮"
    }

    return insights.get(
        common_emotion,
        "No major emotional pattern detected."
    )