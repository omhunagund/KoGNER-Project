import spacy

# Load spaCy model only once
nlp = spacy.load("en_core_web_sm")


def preprocess_text(text: str):
    """
    Preprocess biomedical text using spaCy.

    Returns:
        dict containing cleaned text, tokens,
        lemmas and POS tags.
    """

    doc = nlp(text)

    tokens = []
    lemmas = []
    pos_tags = []

    for token in doc:

        if not token.is_space:

            tokens.append(token.text)

            lemmas.append(token.lemma_)

            pos_tags.append(
                {
                    "Token": token.text,
                    "POS": token.pos_
                }
            )

    cleaned_text = " ".join(tokens)

    return {
    "clean_text": cleaned_text,
    "tokens": tokens,
    "lemmas": lemmas,
    "pos_tags": pos_tags
}