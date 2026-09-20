import json
import hashlib
import re

import faiss
import numpy as np


INPUT_PATH = "data/chunks.json"
INDEX_PATH = "vectorstore/index.faiss"
METADATA_PATH = "vectorstore/metadata.json"

VECTOR_SIZE = 1024


def create_vector(text):
    vector = np.zeros(VECTOR_SIZE, dtype="float32")

    words = re.findall(r"\b[a-zA-Z0-9]+\b", text.lower())

    for word in words:
        hash_value = int(
            hashlib.md5(word.encode("utf-8")).hexdigest(),
            16
        )

        index = hash_value % VECTOR_SIZE
        vector[index] += 1.0

    norm = np.linalg.norm(vector)

    if norm > 0:
        vector = vector / norm

    return vector


with open(INPUT_PATH, "r", encoding="utf-8") as f:
    chunks = json.load(f)


print(f"Creating vectors for {len(chunks)} chunks...")

vectors = np.array(
    [create_vector(chunk["text"]) for chunk in chunks],
    dtype="float32"
)


index = faiss.IndexFlatIP(VECTOR_SIZE)
index.add(vectors)

faiss.write_index(index, INDEX_PATH)


with open(METADATA_PATH, "w", encoding="utf-8") as f:
    json.dump(chunks, f, ensure_ascii=False, indent=2)


print("Index created successfully!")
print(f"Total vectors: {index.ntotal}")
print(f"Saved index to: {INDEX_PATH}")
print(f"Saved metadata to: {METADATA_PATH}")