GENERATE_STORY_PROMPT = """
You are an expert in creating engaging, mysterious, and fun-to-solve lateral thinking riddles in the style of 
*Black Stories*—short, eerie puzzles where players must reconstruct a hidden story using only yes/no questions.

Your task is to generate **original** Black Stories based on the following examples. Each story should have:
- **A title** that summarizes the scenario.
- **A cryptic backstory** that intrigues players and encourages them to ask questions.
- **A solution** that explains what truly happened.

---

### **Examples**

[
    {
        "title": "The Blind Beggar",
        "backstory": "A blind beggar had a brother who died. What relation was the blind beggar to the brother who died?",
        "solution": "The blind beggar was the sister of her brother who died."
    },
    {
        "title": "The Man in the Field",
        "backstory": "A man is lying dead in a field with an unopened package next to him. There are no other creatures in the field. How did he die?",
        "solution": "The man was a parachutist. His parachute failed to open, leading to his fatal fall."
    },
    {
        "title": "Try Hard",
        "backstory": "A salesman tries too hard to make a sale and ends up dead. What happened?",
        "solution": "The salesman was selling parachutes. To demonstrate their reliability, he used one himself, but it failed, leading to his death."
    },
    {
        "title": "The Drowned Woman",
        "backstory": "A woman is found drowned in her car, which is parked in her driveway. There are no signs of foul play. What happened?",
        "solution": "The woman drove into a lake and managed to escape, but later returned to her car to retrieve something, got trapped, and drowned."
    },
    {
        "title": "The Spaniards",
        "backstory": "A man is found dead with a gunshot wound in a Spanish villa. There are no signs of forced entry, and nothing is stolen. What happened?",
        "solution": "The man was playing Russian roulette and lost."
    }
]
Use the above examples to generate your own Black Stories. Make sure to keep the stories original and engaging!
The solutuion should be a short single sentence that explains the scenario and should be easily understandable and checked for correctness.
Format your response as a structured JSON with the keys "title", "backstory", "solution"
"""
