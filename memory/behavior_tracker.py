def track_behavior(emotions):

    if len(emotions) < 5:

        return "Behavior tracking requires more journal entries."

    recent = emotions[:5]

    sadness_count = recent.count("sadness")

    fear_count = recent.count("fear")

    if sadness_count >= 3:

        return (
            "Frequent sadness detected in recent journals."
        )

    if fear_count >= 3:

        return (
            "Stress or anxiety trend detected recently."
        )

    return "No strong negative behavioral trend detected."