from transformers import pipeline
from config import MODEL_NAME


# Load emotion classification pipeline

emotion_classifier = pipeline(
    task="text-classification",
    model=MODEL_NAME,
    top_k=None
)