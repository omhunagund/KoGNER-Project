from nlp.entity_postprocess import normalize_entities
from models.biobert.model_loader import biomedical_ner


def predict_entities(text: str):
    """
    Run BioBERT prediction.
    """

    predictions = biomedical_ner(text)

    entities = []

    for item in predictions:

        entities.append({

            "Entity": item["word"],

            "Type": item["entity_group"],

            "Confidence": round(item["score"] * 100, 2),

            "Start": item["start"],

            "End": item["end"]

        })

    return normalize_entities(entities)