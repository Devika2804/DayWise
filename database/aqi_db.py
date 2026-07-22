from database.connection import get_connection
import pandas as pd

def save_aqi(aqi_data):

    city = aqi_data["city"]
    aqi = aqi_data["aqi"]
    risk_level = aqi_data["risk_level"]
    connection = get_connection()
    cursor=connection.cursor()
    
    cursor.execute(
        """
        INSERT INTO aqi (
            city,
            aqi,
            risk_level
            
        )
        VALUES (%s, %s, %s)
        """,
        (city, aqi, risk_level)
    )

    connection.commit()
    cursor.close()
    connection.close()




def get_aqi_history(city, days):

    connection = get_connection()

    query = """
        SELECT
            created_at,
            aqi,
            risk_level
     FROM aqi
        WHERE LOWER(city) = LOWER(%s)
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

def get_city_aqi_summary(days):

    connection = get_connection()

    query = """
        SELECT
            INITCAP(city) AS city,
            ROUND(AVG(aqi)::numeric,0) AS avg_aqi,
            MIN(aqi) AS best_aqi
        FROM aqi
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