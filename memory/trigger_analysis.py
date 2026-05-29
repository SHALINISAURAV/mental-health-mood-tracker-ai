def analyze_triggers(text):

    triggers = {
        "exam": "Academic stress trigger detected 📚",
        "deadline": "Workload pressure trigger detected ⏰",
        "lonely": "Loneliness-related emotional trigger detected 💙",
        "relationship": "Relationship-related emotional trigger detected ❤️",
        "money": "Financial stress trigger detected 💸"
    }

    text = text.lower()

    detected = []

    for keyword, message in triggers.items():

        if keyword in text:

            detected.append(message)

    return detected