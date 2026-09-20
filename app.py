import streamlit as st
import sys
import os

# Allow Python to find files inside src/
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from rag import answer_question


st.set_page_config(
    page_title="Enverus RAG Chatbot",
    page_icon="🤖",
    layout="wide"
)


st.title("🤖 Enverus RAG Chatbot")

st.write(
    "Ask questions about the "
    "Agent-as-a-Judge research paper."
)


question = st.text_input(
    "Enter your question:",
    placeholder="What is Agent-as-a-Judge?"
)


if st.button("Ask"):

    if not question.strip():

        st.warning("Please enter a question.")

    else:

        with st.spinner("Searching the document..."):

            answer, results = answer_question(question)

        st.subheader("Answer")

        st.write(answer)

        st.subheader("Retrieved Sources")

        for result in results:

            with st.expander(
                f"Page {result['page']} | "
                f"Chunk {result['chunk_id']} | "
                f"Score {result['score']:.4f}"
            ):

                st.write(result["text"])