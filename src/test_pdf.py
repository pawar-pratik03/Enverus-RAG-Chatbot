import fitz

pdf_path = "data/agent_as_a_judge.pdf"

doc = fitz.open(pdf_path)

print("PDF opened successfully!")
print("Number of pages:", len(doc))

doc.close()