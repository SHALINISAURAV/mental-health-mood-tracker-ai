from collections import Counter


def detect_emotional_pattern(emotions):

    if len(emotions) < 3:

        return "Not enough emotional history yet."

    counter = Counter(emotions)

    most_common = counter.most_common(1)[0]

    emotion = most_common[0]

    count = most_common[1]

    return (
        f"Recurring pattern detected: "
        f"{emotion} appeared {count} times."
    )