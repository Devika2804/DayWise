from modules.weather import get_weather
from modules.aqi import get_aqi

from database.weather_db import save_weather
from database.aqi_db import save_aqi

cities = [
    "Bengaluru",
    "Chennai",
    "Coimbatore",
    "Hyderabad",
    "Mumbai"
]

CITY_MAPPING = {
    "bangaluru": "Bengaluru",
    "bengaluru": "Bengaluru",
    "chennai": "Chennai",
    "coimbatore": "Coimbatore",
    "hyderabad": "Hyderabad",
    "mumbai": "Mumbai"
}

for city in cities:

    print(f"Fetching {city}...")

    weather_data = get_weather(city)

    if weather_data:
        weather_data["city"] = CITY_MAPPING.get(
            weather_data["city"].lower(),
            weather_data["city"]
        )
        save_weather(weather_data)

    aqi_data = get_aqi(city)

    if aqi_data:
        aqi_data["city"] = CITY_MAPPING.get(
            aqi_data["city"].lower(),
            aqi_data["city"]
        )
        save_aqi(aqi_data)