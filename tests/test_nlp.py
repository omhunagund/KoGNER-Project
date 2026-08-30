from nlp.preprocessing import preprocess_text

text = (
    "Metformin is used for Type 2 Diabetes. "
    "BRCA1 mutations increase breast cancer risk."
)

result = preprocess_text(text)

print("\nClean Text\n")
print(result["clean_text"])

print("\nTokens\n")
print(result["tokens"])

print("\nLemmas\n")
print(result["lemmas"])

print("\nPOS Tags\n")
print(result["pos_tags"])