import requests
import os
from dotenv import load_dotenv

load_dotenv()


def get_weather(city_name):

    weather_url="https://api.openweathermap.org/data/2.5/weather"

    params={
    "q": city_name,
    "appid":os.getenv("OPENWEATHER_API_KEY"),
    "units" :"metric"
    }

    response=requests.get(weather_url, params=params)
    data=response.json()
    
    if data["cod"] != 200:
        print(f"❌ Error: {data['message']}")
        return
    


    city = data["name"]

    temperature = data["main"]["temp"]

    wind_speed = data["wind"]["speed"]

    weather = data["weather"][0]["description"]

    humidity=data["main"]["humidity"]

    return {
        "city" : city,
        "temperature" : temperature,
        "wind_speed" : wind_speed,
        "weather":  weather,
        "humidity" : humidity
    }

