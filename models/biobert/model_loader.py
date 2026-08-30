from transformers import pipeline

# Load once when the application starts
biomedical_ner = pipeline(
    task="token-classification",
    model="Clinical-AI-Apollo/Medical-NER",
    aggregation_strategy="simple"
)