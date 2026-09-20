# Enverus RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot built to answer questions from the research paper **"Agent-as-a-Judge: Evaluate Agents with Agents"**.

The project demonstrates a complete document-question-answering pipeline starting from PDF ingestion and text extraction, followed by chunking, vector indexing, similarity-based retrieval, and a Streamlit chatbot interface.

---

## Project Overview

The chatbot allows users to ask questions about the provided Agent-as-a-Judge research paper.

Instead of searching the entire document for every question, the system:

1. Extracts text from the PDF.
2. Splits the document into smaller chunks.
3. Converts chunks into lightweight numerical vector representations.
4. Stores the vectors in a FAISS index.
5. Converts the user's question into the same vector representation.
6. Retrieves the most relevant document chunks.
7. Uses the retrieved context to produce an answer.
8. Displays the answer and retrieved source information through Streamlit.

---

## RAG Workflow

```text
Agent-as-a-Judge PDF
        |
        v
PDF Text Extraction
        |
        v
Page-wise Text
        |
        v
Text Chunking
        |
        v
194 Document Chunks
        |
        v
Vector Representation
        |
        v
FAISS Vector Index
        |
        |
        | <---------------- User Question
        |                         |
        |                         v
        |                 Query Vectorization
        |                         |
        v                         |
Similarity Search <--------------+
        |
        v
Top-5 Relevant Chunks
        |
        v
Retrieved Context
        |
        v
Answer Generation
        |
        v
Answer + Source Pages
        |
        v
Streamlit RAG Chatbot

---

## Technologies Used

- Python
- PyMuPDF
- NumPy
- FAISS
- Streamlit
- JSON
- Git
- GitHub

---

## Installation

Clone the repository:

```bash
git clone https://github.com/pawar-pratik03/Enverus-RAG-Chatbot.git

---

## Evaluation

The question bank was processed through the RAG retrieval pipeline.

Questions **Q5–Q19** were tested using:

```text
evaluation/run_evaluation.py

---

## Project Structure

```text
Enverus-RAG-Chatbot/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── agent_as_a_judge.pdf
│   ├── pages.json
│   └── chunks.json
│
├── diagrams/
│   └── rag_workflow.mmd
│
├── evaluation/
│   ├── question_answers.json
│   ├── retrieved_chunks.json
│   └── run_evaluation.py
│
├── src/
│   ├── test_pdf.py
│   ├── ingest.py
│   ├── chunking.py
│   ├── build_index.py
│   ├── retrieve.py
│   └── rag.py
│
└── vectorstore/
    ├── index.faiss
    └── metadata.json

---

## GitHub Repository

This project is available on GitHub:

https://github.com/pawar-pratik03/Enverus-RAG-Chatbot