import json
import os
import sys

# Allow Python to import files from src/
sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "src"
    )
)

from retrieve import retrieve


QUESTIONS = {
    "Q5": "How much time and cost does Agent-as-a-Judge save compared with three human experts?",

    "Q6": "What are the time and cost results for Human-as-a-Judge, Agent-as-a-Judge, and LLM-as-a-Judge?",

    "Q7": "Which three agentic systems are evaluated in the paper?",

    "Q8": "What are the average cost and average time of OpenHands?",

    "Q9": "Which system has the lowest average cost and which has the highest average cost?",

    "Q10": "What is the Requirements Met (Independent) percentage for GPT-Pilot under Human-as-a-Judge?",

    "Q11": "What is the Task Solve Rate for MetaGPT?",

    "Q12": "What is the black-box alignment rate of Agent-as-a-Judge and LLM-as-a-Judge for OpenHands?",

    "Q13": "What are the OpenHands alignment rates when using ask only, then adding graph, read, and locate?",

    "Q14": "Which search algorithm or configuration achieves the best alignment rate?",

    "Q15": "Which two architectures are most frequently used in DevAI?",

    "Q16": "What is Task 51 Requirement R1?",

    "Q17": "Which human evaluator made the most errors and what was the error percentage on GPT-Pilot?",

    "Q18": "What is a drawback of Human-as-a-Judge?",

    "Q19": "What is the GitHub repository URL for this RAG chatbot?"
}


results = {}

for question_id, question in QUESTIONS.items():

    print(f"Processing {question_id}...")

    retrieved = retrieve(question, top_k=5)

    results[question_id] = {
        "question": question,
        "retrieved_chunks": retrieved
    }


OUTPUT_PATH = os.path.join(
    os.path.dirname(__file__),
    "retrieved_chunks.json"
)


with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(
        results,
        f,
        ensure_ascii=False,
        indent=2
    )


print("\nEvaluation completed.")
print(f"Saved retrieved chunks to: {OUTPUT_PATH}")
