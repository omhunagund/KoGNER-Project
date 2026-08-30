from utils.validation import validate_text

samples = [
    "",
    "Hello",
    "Metformin is used for Type 2 Diabetes."
]

for sample in samples:

    valid, message = validate_text(sample)

    print("=" * 40)
    print(sample)
    print(valid)
    print(message)