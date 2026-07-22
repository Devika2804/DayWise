

import streamlit as st


def render_about():
    st.title("ℹ️ About LifePlus")

    st.markdown(
        '''
LifePlus is an AI-powered lifestyle dashboard that combines
live weather, air quality, historical analytics, and AI-powered
recommendations to help users plan their day.
'''
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("✨ Key Features")
        st.markdown(
            '''
- 🌤 Live Weather
- 🌫 Live AQI
- 🧠 AI Daily Brief
- 🏆 Comfort Score
- 🚶 Walking Recommendation
- ⏰ Best Outdoor Time
- 🍲 Food Suggestion
- ❤️ Health Tip
- 📈 Historical Insights
- 🌍 City Comparison
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
2. Weather and AQI are fetched from live APIs.
3. Gemini AI generates daily recommendations.
4. Weather history is stored in PostgreSQL.
5. Insights visualize historical trends and compare cities.
'''
    )

    st.info(
        "LifePlus helps users quickly understand today's conditions "
        "and make informed daily decisions."
    )
