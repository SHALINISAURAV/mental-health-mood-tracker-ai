from memory.pattern_detector import (
    detect_emotional_pattern
)


def test_pattern_detection():

    emotions = [
        "fear",
        "fear",
        "sadness",
        "fear"
    ]

    result = detect_emotional_pattern(
        emotions
    )

    assert "fear" in result