from database.connection import get_connection
import pandas as pd

def save_weather(weather_data):

    city = weather_data["city"]
    temperature = weather_data["temperature"]
    humidity = weather_data["humidity"]
    wind_speed = weather_data["wind_speed"]
    weather = weather_data["weather"]

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO weather (
            city,
            temperature,
            humidity,
            wind_speed,
            weather
        )
        VALUES (%s, %s, %s, %s, %s)
        """,
        (city, temperature, humidity, wind_speed, weather)
    )

    connection.commit()

    cursor.close()
    connection.close()

def get_weather_history(city, days):
    connection = get_connection()

    query = """
        SELECT
            created_at,
            temperature,
            humidity,
            weather
        FROM weather
        WHERE city = %s
          AND created_at >= NOW() - INTERVAL %s
        ORDER BY created_at
    """

    df = pd.read_sql(
        query,
        connection,
        params=(city, f"{days} days")
    )

    connection.close()

    return df

def get_city_temperature_summary(days):

    connection = get_connection()

    query = """
        SELECT
            city,
            ROUND(AVG(temperature)::numeric,1) AS avg_temp,
            ROUND(MAX(temperature)::numeric,1) AS max_temp,
            AVG(humidity) AS avg_humidity
        FROM weather
        WHERE created_at >= NOW() - INTERVAL %s
        GROUP BY city
        ORDER BY city
    """

    df = pd.read_sql(
        query,
        connection,
        params=(f"{days} days",)
    )

    connection.close()

    return df