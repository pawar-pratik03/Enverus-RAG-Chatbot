import json

INPUT_PATH = "data/pages.json"
OUTPUT_PATH = "data/chunks.json"

CHUNK_SIZE = 800
CHUNK_OVERLAP = 100


with open(INPUT_PATH, "r", encoding="utf-8") as f:
    pages = json.load(f)


chunks = []

chunk_id = 0

for page in pages:
    page_number = page["page"]
    text = page["text"]

    start = 0

    while start < len(text):
        end = start + CHUNK_SIZE
        chunk_text = text[start:end].strip()

        if chunk_text:
            chunks.append({
                "chunk_id": chunk_id,
                "page": page_number,
                "text": chunk_text
            })

            chunk_id += 1

        start += CHUNK_SIZE - CHUNK_OVERLAP


with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(chunks, f, ensure_ascii=False, indent=2)


print(f"Created {len(chunks)} chunks.")
print(f"Saved to: {OUTPUT_PATH}")