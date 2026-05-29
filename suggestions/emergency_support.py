EMERGENCY_KEYWORDS = [

    "suicide",
    "self harm",
    "kill myself",
    "hopeless",
    "worthless"
]


def detect_emergency(text):

    text = text.lower()

    for keyword in EMERGENCY_KEYWORDS:

        if keyword in text:

            return True

    return False