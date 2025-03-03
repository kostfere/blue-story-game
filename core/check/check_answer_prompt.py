CHECK_ANSWER_PROMPT_TEMPLATE = """Compare the user-provided fact with the hidden fact in this story:
Backstory: {backstory}
Hidden Fact: {answer}
Does '{user_fact}' match the hidden fact?

Respond with:
- 'Yes' if the user's fact correctly conveys the main idea or essence of the hidden fact, even if minor details differ.
- 'Yes but incomplete' if an important part of the hidden fact is missing or significantly altered.
- 'No' if the user's fact is incorrect or does not align with the hidden fact in a meaningful way.
"""
