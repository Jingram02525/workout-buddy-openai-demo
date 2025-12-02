"""
Workout Buddy - OpenAI Demo

Simple CLI app that turns a few user inputs into a prompt
and asks OpenAI for a workout plan.

Run with:
    python workout_buddy.py
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. Load environment variables from .env
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError(
        "OPENAI_API_KEY not found. "
        "Create a .env file and add OPENAI_API_KEY=your_api_key_here"
    )

# 2. Create OpenAI client
client = OpenAI(api_key=api_key)


def build_prompt(name, goal, fitness_level, equipment, minutes_per_day):
    """Turn user answers into a single prompt string."""
    prompt = f"""
You are a friendly, encouraging personal trainer called Workout Buddy.

Create a simple, safe workout plan for this person:

Name: {name}
Goal: {goal}
Fitness level: {fitness_level}
Available equipment: {equipment}
Minutes per day: {minutes_per_day}

Requirements:
- 3-day weekly plan (Day 1, Day 2, Day 3)
- For each day, list 4–6 simple exercises
- Use bodyweight or very basic movements only
- Include a super short warm-up and cool-down
- Keep it under 400 words
- Speak directly to {name} in a supportive voice
"""
    return prompt.strip()


def get_workout_plan(prompt: str) -> str:
    """
    Call OpenAI's Responses API with a simple text prompt.

    We use response.output_text for convenience so students
    don't have to dig through the full JSON.
    """
    response = client.responses.create(
        model="gpt-5.1-mini",  # you can swap models later
        input=prompt,
    )

    # The SDK exposes a helper that returns the main text content
    return response.output_text


def main():
    print("=" * 50)
    print(" Welcome to Workout Buddy (OpenAI Demo) ")
    print("=" * 50)

    # Collect minimal info from the user
    name = input("What is your name? ")
    goal = input("What is your main goal? (e.g. lose weight, get stronger, more energy): ")
    fitness_level = input("What is your fitness level? (beginner / intermediate / advanced): ")
    equipment = input("What equipment do you have? (e.g. none, dumbbells, resistance bands): ")
    minutes_per_day = input("How many minutes per day can you work out? ")

    print("\nGreat! Creating your workout plan with OpenAI...\n")

    prompt = build_prompt(name, goal, fitness_level, equipment, minutes_per_day)
    plan = get_workout_plan(prompt)

    print("=" * 50)
    print(" Your Personalized Workout Plan ")
    print("=" * 50)
    print(plan)
    print("=" * 50)
    print("Remember: go at your own pace and listen to your body.")
    print("=" * 50)


if __name__ == "__main__":
    main()
