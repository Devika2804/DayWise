from google import genai
from datetime import datetime
import json
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

current_hour = datetime.now().hour


def get_ai_brief(
    city,
    weather,
    temperature,
    aqi,
    risk_level
):

    current_hour = datetime.now().hour

    if current_hour < 12:
        time_of_day = "morning"
    elif current_hour < 17:
        time_of_day = "afternoon"
    else:
        time_of_day = "evening"

    prompt = f"""
City: {city}
Weather: {weather}
Temperature: {temperature}
AQI: {aqi}
Risk Level: {risk_level}
Time Of Day: {time_of_day}

You are an AI daily companion.

Generate a premium mobile-app briefing.

Rules:

- Maximum 3 short sentences for brief
- Mention weather
- Mention AQI
- Mention one useful recommendation
- Mention food suggestion naturally
- No movie suggestions
- Keep under 60 words

Walking Recommendation Rules:
- Return a friendly title
- Give 2 short reasons

Things To Carry Rules:
- Always include 💧 Water Bottle
- Use emojis
- Maximum 4 items

Best Outdoor Time Rules:
- Give a realistic time range
- Example: 7 AM - 10 AM
- Give one short reason
Return ONLY valid JSON.

{{
    "brief": "Daily briefing",
    
    "walking_title":"🚶Good time for walk",
    "walking_reason_1": "Reason 1",
    "walking_reason_2": "Reason 2",

    "best_outdoor_time": "Best time to go outside",
    "best_outdoor_time_reason": "Why this time suits today",    
    "food": "Food recommendation",
    "food_reason": "Why this food suits today's weather",

    "health_tip": "two health tip",


    "things_to_carry": [
        "💧 Water Bottle",
        "☂️ Umbrella"
    ]
}}
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        text = response.text.strip()

        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

        return json.loads(text)

    except Exception as e:

        print(e)

        return {
    "brief": (
        f"Good {time_of_day}. "
        f"{city} is currently {temperature}°C with {weather}. "
        f"AQI is {aqi} ({risk_level}). Stay hydrated today."
    ),
    "walking_title":"🚶Good time for walk",
    "walking_reason_1": "Pleasant temperature",
    "walking_reason_2": "Good air quality",

    "best_outdoor_time": "7 AM - 10 AM",
    "best_outdoor_time_reason": "Cool temperatures and good air quality.",

    "food": "Ven Pongal",
    "food_reason": "Comforting and suitable for today's weather.",

    "health_tip": "💧 Stay hydrated throughout the day.",


    "things_to_carry": [
        "💧 Water Bottle"
    ]
}