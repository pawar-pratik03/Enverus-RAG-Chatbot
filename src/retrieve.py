import json
import re
import hashlib

import faiss
import numpy as np


INDEX_PATH = "vectorstore/index.faiss"
METADATA_PATH = "vectorstore/metadata.json"

VECTOR_SIZE = 1024


def tokenize(text):
    return set(
        re.findall(r"\b[a-zA-Z0-9]+\b", text.lower())
    )


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


index = faiss.read_index(INDEX_PATH)

with open(METADATA_PATH, "r", encoding="utf-8") as f:
    chunks = json.load(f)


def retrieve(query, top_k=5):

    query_vector = create_vector(query).reshape(1, -1)

    # Retrieve more candidates first
    scores, indices = index.search(
        query_vector,
        min(20, len(chunks))
    )

    query_words = tokenize(query)

    candidates = []

    for faiss_score, idx in zip(scores[0], indices[0]):

        if idx == -1:
            continue

        chunk = chunks[idx]

        chunk_words = tokenize(chunk["text"])

        overlap = len(query_words.intersection(chunk_words))

        if query_words:
            keyword_score = overlap / len(query_words)
        else:
            keyword_score = 0

        # Combine semantic-style hash score and keyword overlap
        final_score = (
            0.4 * float(faiss_score)
            + 0.6 * keyword_score
        )

        candidates.append({
            "score": final_score,
            "faiss_score": float(faiss_score),
            "keyword_score": keyword_score,
            "chunk_id": chunk["chunk_id"],
            "page": chunk["page"],
            "text": chunk["text"]
        })

    candidates.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return candidates[:top_k]


if __name__ == "__main__":

    query = input("Enter your question: ")

    results = retrieve(query)

    print("\nRetrieved chunks:\n")

    for result in results:

        print("=" * 60)
        print(f"Chunk ID: {result['chunk_id']}")
        print(f"Page: {result['page']}")
        print(f"Final Score: {result['score']:.4f}")
        print(f"Keyword Score: {result['keyword_score']:.4f}")
        print(result["text"][:500])