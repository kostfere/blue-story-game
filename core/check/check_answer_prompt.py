CHECK_ANSWER_PROMPT_TEMPLATE = """Compare the user-provided fact with the hidden fact in this story:
Backstory: {backstory}
Hidden Fact: {answer}
Does '{user_fact}' match the hidden fact?
"""
