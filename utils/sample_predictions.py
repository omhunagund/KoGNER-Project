import pandas as pd


def get_sample_predictions():
    """
    Temporary placeholder predictions.
    These will later be replaced by BioBERT output.
    """

    entities = [
        {
            "Entity": "Metformin",
            "Type": "Drug",
            "Confidence": "98%"
        },
        {
            "Entity": "Type 2 Diabetes",
            "Type": "Disease",
            "Confidence": "99%"
        },
        {
            "Entity": "BRCA1",
            "Type": "Gene",
            "Confidence": "97%"
        },
        {
            "Entity": "Breast Cancer",
            "Type": "Disease",
            "Confidence": "98%"
        },
        {
            "Entity": "Aspirin",
            "Type": "Drug",
            "Confidence": "96%"
        }
    ]

    return pd.DataFrame(entities)