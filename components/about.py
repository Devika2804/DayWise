

import streamlit as st


def render_about():
    st.title("💡 About DayWise")

    st.markdown(
        '''
DayWise helps users understand today's weather and air quality
through simple AI-powered insights, making it easier to plan
outdoor activities, travel, exercise, and daily routines.
'''
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("✨ Key Features")
        st.markdown(
            '''
🌤 Live Weather
🌫 Air Quality Index (AQI)
🤖 AI Daily Summary
🏆 Comfort Score
🚶 Outdoor Activity Recommendation
⏰ Best Time to Go Outside
🍽 Food Suggestion
❤️ Health Tips
📈 Historical Trends
🌍 Compare Citiesn
'''
        )

    with col2:
        st.subheader("🛠 Technology Stack")
        st.markdown(
            '''
- Python
- Streamlit
- PostgreSQL
- Plotly
- Google Gemini
- OpenWeather API
- AQI API
'''
        )

    st.divider()

    st.subheader("📊 How It Works")

    st.markdown(
        '''
1. Select a city.
2. Fetch live weather and AQI data.
3. Generate AI-powered daily insights.
4. Store weather history in PostgreSQL.
5. Explore trends and compare cities.
'''
    )

    st.info(
    "Make smarter everyday decisions with real-time weather, air quality, and AI-powered recommendations."
)
