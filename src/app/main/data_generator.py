"""
Codespaces‑safe generator for a 20,000‑record library dataset.
Run manually:
    uv run python src/app/main/data_generator.py
"""

from faker import Faker
import json
from pathlib import Path
import random
import time

fake = Faker()
Faker.seed(12345)
random.seed(12345)

OUTPUT_PATH = Path(__file__).parent / "data.json"
TOTAL = 20_000
CHUNK = 2_000  # write in chunks to avoid Codespaces freezing

CATEGORIES = [
    "Fiction", "Non‑Fiction", "Science", "History", "Biography",
    "Fantasy", "Mystery", "Technology", "Education", "Art"
]

ITEM_TYPES = ["Book", "eBook", "Magazine", "Journal", "Audio Book"]

def generate_record():
    return {
        "title": fake.sentence(nb_words=4).rstrip("."),
        "author": fake.name(),
        "year": int(fake.year()),
        "isbn": fake.isbn13(),
        "category": random.choice(CATEGORIES),
        "type": random.choice(ITEM_TYPES),
        "summary": fake.text(max_nb_chars=200),
    }

def generate_dataset():
    print(f"📚 Generating {TOTAL:,} records…")
    data = []

    for i in range(1, TOTAL + 1):
        data.append(generate_record())

        if i % CHUNK == 0:
            print(f"   Writing chunk {i - CHUNK + 1:,}–{i:,}…")
            OUTPUT_PATH.write_text(json.dumps(data, indent=2))
            time.sleep(0.1)  # prevent Codespaces CPU spike

    OUTPUT_PATH.write_text(json.dumps(data, indent=2))
    print(f"🎉 Dataset saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    generate_dataset()

