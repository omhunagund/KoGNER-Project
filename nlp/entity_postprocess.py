LABEL_MAPPING = {

    # -----------------------------
    # Clinical-AI-Apollo Labels
    # -----------------------------

    "MEDICATION": "DRUG",
    "DISEASE_DISORDER": "DISEASE",
    "DIAGNOSTIC_PROCEDURE": "PROCEDURE",
    "THERAPEUTIC_PROCEDURE": "THERAPY",
    "SIGN_SYMPTOM": "SYMPTOM",
    "BIOLOGICAL_STRUCTURE": "BIOLOGICAL_STRUCTURE",
    "DETAILED_DESCRIPTION": "BIOLOGICAL_STRUCTURE",

    # -----------------------------
    # Previous BioBERT Labels
    # (kept for compatibility)
    # -----------------------------

    "Medication": "DRUG",
    "Disease_disorder": "DISEASE",
    "Diagnostic_procedure": "PROCEDURE",
    "Biological_structure": "BIOLOGICAL_STRUCTURE",
    "Therapeutic_procedure": "THERAPY",
    "Sign_symptom": "SYMPTOM"
}


def normalize_entities(entities):
    """
    Normalize entity labels across different biomedical NER models.
    """

    normalized = []
    seen = set()

    for entity in entities:

        entity_name = entity["Entity"].replace("##", "").strip()

        entity_type = LABEL_MAPPING.get(
            entity["Type"],
            entity["Type"]
        )

        key = (
            entity_name.lower(),
            entity_type
        )

        if key in seen:
            continue

        seen.add(key)

        normalized.append({

            "Entity": entity_name,

            "Type": entity_type,

            "Confidence": entity["Confidence"],

            "Start": entity["Start"],

            "End": entity["End"]

        })

    normalized.sort(
        key=lambda x: x["Start"]
    )

    return normalized