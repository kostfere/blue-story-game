import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

from core.game import ask_question, check_fact, generate_mystery

# 🔴 Set page config at the very top (before any other Streamlit commands)
st.set_page_config(page_title="Black Stories Puzzle Game", layout="wide")

# Load .env file if available
load_dotenv()


# Sidebar for API key input
def setup_sidebar():
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

    return openai_api_key


def show_game_instructions():
    """Display how to play instructions."""
    with st.expander("ℹ️ How to Play"):
        st.markdown("""
        - 🕵️ The game will generate a **mystery story** with a **hidden fact**.
        - ❓ You can ask **yes/no** questions to gather clues about the story.
        - 🎯 When you think you know the answer, **submit your final guess**.
        - ✅ If your guess is correct, you win! Otherwise, keep asking questions.
        - 🔎 **Want to cheat?** Click "Reveal the Hidden Fact" to see the solution.
        """)


def initialize_session_state():
    """Initialize session state variables for the game."""
    if "mystery" not in st.session_state:
        st.session_state.mystery = None
    if "questions" not in st.session_state:
        st.session_state.questions = []
    if "solved" not in st.session_state:
        st.session_state.solved = False


def display_mystery():
    """Display the generated mystery title and backstory."""
    if st.session_state.mystery:
        st.subheader("📜 Story:")
        st.markdown(f"### {st.session_state.mystery.title}")
        st.write(st.session_state.mystery.backstory)


def handle_generate_mystery(client):
    """Handle generating a new mystery."""
    if st.button("🕵️ Generate New Mystery"):
        try:
            st.session_state.mystery = generate_mystery(client)
            st.session_state.questions = []
            st.session_state.solved = False
        except Exception as e:
            st.error(f"❌ Failed to generate mystery: {e}")


def handle_question_asking(client):
    """Handle asking yes/no questions."""
    if st.session_state.mystery:
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


def handle_guess_submission(client):
    """Handle user submitting their final guess."""
    if st.session_state.mystery:
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


def reveal_hidden_fact():
    """Allow users to reveal the hidden solution."""
    if st.session_state.mystery:
        with st.expander("🕵️‍♂️ Reveal the Hidden Fact"):
            st.subheader("🔎 Hidden Fact:")
            st.write(st.session_state.mystery.answer)  # Ensure correct attribute


# Main UI
def main():
    st.title("🧠 Black Stories Puzzle Game")

    # Setup and validate API key
    openai_api_key = setup_sidebar()

    # Initialize OpenAI client
    client = OpenAI(api_key=openai_api_key)

    # Show game instructions
    show_game_instructions()

    # Initialize session state
    initialize_session_state()

    # Generate a new mystery
    handle_generate_mystery(client)

    # Display mystery (if exists)
    display_mystery()

    # Handle question asking
    handle_question_asking(client)

    # Handle guess submission
    handle_guess_submission(client)

    # Allow revealing the hidden fact
    reveal_hidden_fact()


if __name__ == "__main__":
    main()
