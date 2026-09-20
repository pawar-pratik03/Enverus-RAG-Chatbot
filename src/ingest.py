import pymupdf
import json

PDF_PATH = "data/agent_as_a_judge.pdf"
OUTPUT_PATH = "data/pages.json"

doc = pymupdf.open(PDF_PATH)

pages = []

for page_number, page in enumerate(doc, start=1):
    text = page.get_text("text").strip()

    pages.append({
        "page": page_number,
        "text": text
    })

doc.close()

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(pages, f, ensure_ascii=False, indent=2)

print(f"Successfully extracted {len(pages)} pages.")
print(f"Saved to: {OUTPUT_PATH}")