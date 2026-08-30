from models.biobert.predict import predict_entities

text = (
    "Metformin is used for Type 2 Diabetes. "
    "BRCA1 mutations increase breast cancer risk."
)

results = predict_entities(text)

for entity in results:
    print(entity)