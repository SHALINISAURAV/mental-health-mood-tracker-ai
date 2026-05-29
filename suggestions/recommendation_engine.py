import random

from suggestions.coping_strategies import (
    COPING_STRATEGIES
)

from suggestions.wellness_tips import (
    WELLNESS_TIPS
)


def generate_recommendations(emotion):

    strategies = COPING_STRATEGIES.get(
        emotion,
        []
    )

    random_tip = random.choice(
        WELLNESS_TIPS
    )

    return {
        "strategies": strategies,
        "wellness_tip": random_tip
    }