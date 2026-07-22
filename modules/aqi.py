import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

AQI_API_KEY = os.getenv("AQI_API_KEY")

if AQI_API_KEY is None:
    AQI_API_KEY = st.secrets["AQI_API_KEY"]

def get_aqi(city_name):


    aqi_url=f"https://api.waqi.info/feed/{city_name}/"

    params={
        "token" : AQI_API_KEY
    }

    response=requests.get(aqi_url,params=params)
    data=response.json()
    
    if data["status"] != "ok":
        print(f"❌ Error: {data['data']}")
        return
    
    city = city_name
    aqi=data["data"]["aqi"]
    risk_level=get_risk_level(aqi)
    
    
    return {
    "city": city,
    "aqi": aqi,
    "risk_level": risk_level
}

def get_risk_level(aqi):

    if aqi <= 50:
        return "Low"

    elif aqi <= 100:
        return "Moderate"

    elif aqi <= 150:
        return "Medium"

    elif aqi <= 200:
        return "High"

    else:
        return "Very High"
    
    

    



