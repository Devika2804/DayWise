
import streamlit as st
from modules.weather import get_weather
from modules.aqi import get_aqi
from modules.ai_brief import get_ai_brief

def calculate_comfort_score(temp, humidity, aqi):
    score = 100
    if temp > 38:
        score -= 30
    elif temp > 34:
        score -= 20
    elif temp > 30:
        score -= 10
    if humidity > 85:
        score -= 15
    elif humidity > 70:
        score -= 8
    if aqi > 200:
        score -= 30
    elif aqi > 150:
        score -= 20
    elif aqi > 100:
        score -= 10
    elif aqi > 50:
        score -= 5
    return max(score,0)

def render_home(city_name):
    with st.spinner("Fetching weather data..."):
         weather_data = get_weather(city_name)
         aqi_data = get_aqi(city_name)

    if not weather_data or not aqi_data:
        st.error("Unable to fetch weather or AQI data.")
        return

    weather = weather_data["weather"]
    temp = weather_data["temperature"]
    humidity = weather_data["humidity"]
    aqi = aqi_data["aqi"]
    risk = aqi_data["risk_level"]

    ai = get_ai_brief(city_name, weather, temp, aqi, risk)
    comfort = calculate_comfort_score(temp, humidity, aqi)

    st.markdown(f"# 📍 {city_name}")
    st.markdown(f"##### ☁️ {weather.title()} | 🌡 {temp}°C | 💧 {humidity}% | 🌫 AQI {aqi}")

    st.markdown("## 🧠 AI Daily Brief")
    st.info(ai["brief"])

    st.markdown("### Today's Overview")
    c1,c2,c3 = st.columns(3)
    with c1:
        st.markdown("#### 🏆 Comfort Score")
        st.markdown(f"##### {comfort}/100")
    with c2:
        st.markdown(f"#### {ai['walking_title']}")
        st.write("✅", ai["walking_reason_1"])
        st.write("✅", ai["walking_reason_2"])
    with c3:
        st.markdown("#### ⏰ Best Outdoor Time")
        st.write(ai["best_outdoor_time"])
        st.caption(ai["best_outdoor_time_reason"])

    st.divider()
    st.markdown("### ✨ Recommendations")
    c1,c2,c3 = st.columns(3)
    with c1:
        st.markdown("#### 🎒 Things To Carry")
        for item in ai["things_to_carry"]:
            st.write(item)
    with c2:
        st.markdown("#### 🍲 Food Suggestion")
        st.write(ai["food"])
        st.caption(ai["food_reason"])
    with c3:
        st.markdown("#### ❤️ Health Tip")
        st.write(ai["health_tip"])
