import streamlit as st
import os
from dotenv import load_dotenv
from core.game import generate_mystery, ask_question, check_fact
from openai import OpenAI

# 🔴 Set page config at the very top (before any other Streamlit commands)
st.set_page_config(page_title="Lateral Thinking Puzzle Game", layout="wide")

# Load .env file if available
load_dotenv()

# Sidebar for API key input
with st.sidebar:
    st.header("🔑 API Configuration")
    
    # Get API key from env variable or user input
    openai_api_key = st.text_input("OpenAI API Key", key="openai_api_key", type="password")
    
    # Links for API key help
    st.markdown("[Get an OpenAI API key](https://platform.openai.com/account/api-keys)")

# Use environment variable if user didn’t enter an API key manually
if not openai_api_key:
    openai_api_key = os.getenv("OPENAI_API_KEY")

# Validate API Key
if not openai_api_key:
    st.error("❌ Please enter an OpenAI API Key to use this app.")
    st.stop()  # Stop execution if no key is provided

# Initialize OpenAI client
client = OpenAI(api_key=openai_api_key)

# Main UI
def main():
    st.title("🧠 Lateral Thinking Puzzle Game")
    
    # 📌 **User Instructions Section**
    with st.expander("ℹ️ How to Play"):
        st.markdown("""
        - 🕵️ The game will generate a **mystery story** with a **hidden fact**.
        - ❓ You can ask **yes/no** questions to gather clues about the story.
        - 🎯 When you think you know the answer, **submit your final guess**.
        - ✅ If your guess is correct, you win! Otherwise, keep asking questions.
        - 🔎 **Want to cheat?** Click "Reveal the Hidden Fact" to see the solution.
        """)

    # Initialize session state variables
    if "mystery" not in st.session_state:
        st.session_state.mystery = None
    if "questions" not in st.session_state:
        st.session_state.questions = []
    if "solved" not in st.session_state:
        st.session_state.solved = False

    # Button to generate a new mystery
    if st.button("🕵️ Generate New Mystery"):
        try:
            st.session_state.mystery = generate_mystery(client)
            st.session_state.questions = []
            st.session_state.solved = False
        except Exception as e:
            st.error(f"❌ Failed to generate mystery: {e}")

    # Display the mystery backstory if it exists
    if st.session_state.mystery:
        st.subheader("📜 Story:")
        st.write(st.session_state.mystery.backstory)

        # Input for yes/no questions
        st.subheader("❓ Ask Yes/No Questions")
        user_question = st.text_input("Enter your question:", key="question_input")
        if st.button("🔍 Ask"):
            try:
                answer = ask_question(client, user_question, st.session_state.mystery)
                st.session_state.questions.append((user_question, answer))
            except Exception as e:
                st.error(f"❌ Error answering question: {e}")

        # Display previous questions and answers
        if st.session_state.questions:
            st.subheader("📜 Previous Questions:")
            for idx, (q, a) in enumerate(st.session_state.questions, start=1):
                st.write(f"**Q{idx}:** {q}  **A:** {a}")

        # Input for submitting final guess
        st.subheader("🎯 Submit Your Guess")
        user_fact = st.text_input("What do you think the hidden fact is?", key="fact_input")
        if st.button("✅ Submit Guess"):
            try:
                is_correct = check_fact(client, user_fact, st.session_state.mystery)
                if is_correct:
                    st.success("🎉 Correct! You solved the mystery!")
                    st.session_state.solved = True
                else:
                    st.error("❌ Incorrect. Keep trying!")
            except Exception as e:
                st.error(f"❌ Error checking guess: {e}")

        # 🔎 **Always Allow User to Reveal Hidden Fact**
        with st.expander("🕵️‍♂️ Reveal the Hidden Fact"):
            if st.session_state.mystery:
                st.subheader("🔎 Hidden Fact:")
                st.write(st.session_state.mystery.answer)

if __name__ == "__main__":
    main()