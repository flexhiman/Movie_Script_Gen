import json
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Use getenv for API
TEST_OPENAI_API_KEY = os.getenv("TEST_OPENAI_API_KEY")


def get_llm_response(user_prompt, system_prompt):
    client = OpenAI(
        api_key=TEST_OPENAI_API_KEY,
    )

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
    )

    return completion.choices[0].message.content


def generate_movie_script(prompt, universe):
    chatgpt_prompt = (
        f"{prompt} Characters: {', '.join(universe['characters'])}. "
        f"Locations: {', '.join(universe['locations'])}. "
        f"Emotions: {', '.join(universe['emotions'])}."
    )

    chatgpt_response = get_llm_response(chatgpt_prompt, "Initial Emotion: neutral")

    scenes = []
    current_scene = {"location": ', '.join(universe['locations']) if universe['locations'] else 'default',
                     "characters": universe['characters'] if universe['characters'] else [], "dialogue": []}

    for sentence in chatgpt_response.split('.'):
        sentence = sentence.strip()
        if sentence:
            emotion = determine_emotion(sentence)
            speaker = universe['characters'][len(current_scene["dialogue"]) % len(universe['characters'])]
            current_scene["dialogue"].append({
                "speaker": speaker,
                "text": sentence,
                "emotion": emotion
            })

    scenes.append(current_scene)
    generated_script = {"scenes": scenes}

    return generated_script

# TODO optimize
def determine_emotion(sentence):
    # Example: Check for words related to emotions in the sentence
    if any(word in sentence.lower() for word in ["surprised", "smirking", "grinning", "smiling", "smile", "happy", "happiness"]):
        return "happiness"
    elif "sad" in sentence.lower():
        return "sadness"
    elif "angry" in sentence.lower():
        return "anger"
    elif "disappointed" in sentence.lower():
        return "disappointment"
    # Add other conditions as needed

    # Default to "neutral"
    return "neutral"


if __name__ == "__main__":
    user_input = input("Enter the scenario topic: ")
    characters_input = input("Enter character names separated by commas: ")
    locations_input = input("Enter location names separated by commas: ")
    emotions_input = input("Enter emotions separated by commas: ")

    characters = [char.strip() for char in characters_input.split(',')]
    locations = [loc.strip() for loc in locations_input.split(',')]
    emotions = [emo.strip() for emo in emotions_input.split(',')]

    user_universe = {
        "characters": characters,
        "locations": locations,
        "emotions": emotions
    }

    generated_script = generate_movie_script(user_input, user_universe)
    print(json.dumps(generated_script, indent=4, ensure_ascii=False))
