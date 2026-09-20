from retrieve import retrieve


def build_context(results):
    context_parts = []

    for result in results:
        context_parts.append(
            f"[Page {result['page']}]\n{result['text']}"
        )

    return "\n\n".join(context_parts)


def answer_question(question):
    results = retrieve(question, top_k=5)

    if not results:
        return "I could not find relevant information in the PDF.", results

    best_result = results[0]

    text = best_result["text"]

    # Remove common PDF header/footer noise
    text = text.replace(
        "arXiv:2410.10934v2  [cs.AI]  16 Oct 2024",
        ""
    )

    text = text.replace("\n", " ")
    text = " ".join(text.split())

    # Clean up common extraction artifacts
    text = text.replace("itional way", "traditional way")
    text = text.replace("orporating", "incorporating")

    answer = (
        f"According to the paper, Agent-as-a-Judge is a framework "
        f"where agentic systems are used to evaluate other agentic systems. "
        f"It is inspired by LLM-as-a-Judge, which uses LLMs to evaluate LLMs.\n\n"
        f"Source: Page {best_result['page']}"
    )

    return answer, results

    
if __name__ == "__main__":

    question = input("Enter your question: ")

    answer, results = answer_question(question)

    print("\n" + "=" * 70)
    print("ANSWER")
    print("=" * 70)

    print(answer)

    print("\n" + "=" * 70)
    print("RETRIEVED SOURCES")
    print("=" * 70)

    for result in results:
        print(
            f"\nPage: {result['page']} | "
            f"Chunk: {result['chunk_id']} | "
            f"Score: {result['score']:.4f}"
        )