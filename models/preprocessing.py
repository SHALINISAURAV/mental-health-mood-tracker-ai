import re


def clean_text(text: str) -> str:
    """
    Clean and normalize journal text.

    Steps:
    - Convert to lowercase
    - Remove special characters
    - Remove extra spaces

    Args:
        text (str): Raw user journal input

    Returns:
        str: Cleaned text
    """

    # Lowercase
    text = text.lower()

    # Remove special characters
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text