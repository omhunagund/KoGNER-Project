"""
Validation utilities for KoGNER.
"""


def validate_text(text: str):
    """
    Validate biomedical input text.

    Returns:
        (is_valid, message)
    """

    if text is None:
        return False, "Input text cannot be empty."

    text = text.strip()

    if len(text) == 0:
        return False, "Please enter biomedical text."

    if len(text) < 10:
        return False, "Input text is too short."

    if len(text) > 10000:
        return False, "Input text is too long."

    return True, "Valid input."