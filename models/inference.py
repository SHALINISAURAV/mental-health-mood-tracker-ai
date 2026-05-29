from models.preprocessing import clean_text
from models.emotion_model import emotion_classifier


def predict_emotion(text: str) -> list:
    """
    Predict emotions from user journal text.

    Args:
        text (str): Raw journal input

    Returns:
        list: Emotion predictions with scores
    """

    # Clean text
    cleaned_text = clean_text(text)

    # Run model inference
    predictions = emotion_classifier(cleaned_text)

    return predictions[0]