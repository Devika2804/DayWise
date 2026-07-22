import streamlit as st
import plotly.express as px

from database.weather_db import get_weather_history, get_city_temperature_summary
from database.aqi_db import get_aqi_history, get_city_aqi_summary



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

    return max(score, 0)


def render_insights(city_name):

    st.title("📈 Insights")

    h1, h2 = st.columns([4, 1])

    with h1:
        st.subheader(f"Viewing insights for {city_name}")

    with h2:
        period = st.selectbox(
            "Period",
            ["Last 7 Days", "Last 30 Days", "Last 90 Days"]
        )

    days = {
        "Last 7 Days": 7,
        "Last 30 Days": 30,
        "Last 90 Days": 90
    }[period]

    weather_df = get_weather_history(city_name, days)
    aqi_df = get_aqi_history(city_name, days)

    st.subheader("📅 Weekly Highlights")
    h1, h2, h3, h4 = st.columns(4)
    
    hottest = weather_df.loc[weather_df["temperature"].idxmax()]
    coolest = weather_df.loc[weather_df["temperature"].idxmin()]

    best_aqi = aqi_df.loc[aqi_df["aqi"].idxmin()]
    worst_aqi = aqi_df.loc[aqi_df["aqi"].idxmax()]

    if not weather_df.empty and not aqi_df.empty:
          with h1:
             st.metric(
               "🔥 Hottest Day",
                 f"{hottest['temperature']:.1f}°C",
                 hottest["created_at"].strftime("%A")
    )

          with h2:
             st.metric(
            "❄️ Coolest Day",
             f"{coolest['temperature']:.1f}°C",
             coolest["created_at"].strftime("%A")
    )

          with h3:
             st.metric(
            "🌫 Best AQI",
             best_aqi["aqi"],
             best_aqi["created_at"].strftime("%A")
    )

          with h4:
            st.metric(
             "⚠️ Worst AQI",
             worst_aqi["aqi"],
             worst_aqi["created_at"].strftime("%A")
    )

    c1, c2 = st.columns(2)

    with c1:
        st.subheader("🌡 Temperature Trend")
        if weather_df.empty:
            st.info("No weather data available.")
        else:
            st.line_chart(weather_df, x="created_at", y="temperature")

    with c2:
        st.subheader("🌫 AQI Trend")
        if aqi_df.empty:
            st.info("No AQI data available.")
        else:
            st.line_chart(aqi_df, x="created_at", y="aqi")

    st.divider()

    temp_summary = get_city_temperature_summary(days)
    aqi_summary = get_city_aqi_summary(days)

    temp_summary["city"] = temp_summary["city"].str.strip().str.title()
    aqi_summary["city"] = aqi_summary["city"].str.strip().str.title()

    comparison = temp_summary.merge(aqi_summary, on="city")

    comparison["comfort_score"] = comparison.apply(
        lambda r: calculate_comfort_score(
            r["avg_temp"],
            60,
            r["avg_aqi"]
        ),
        axis=1
    )

    comparison = comparison.sort_values("comfort_score")

    st.subheader("🌍 City Comparison")

    fig = px.bar(
        comparison,
        x="comfort_score",
        y="city",
        orientation="h",
        text="comfort_score",
        color="comfort_score",
        color_continuous_scale="RdYlGn"
    )

    fig.update_layout(
        coloraxis_showscale=False,
        height=350,
        margin=dict(l=20, r=20, t=20, b=20)
    )

    st.plotly_chart(fig, use_container_width=True)

    with st.expander("View comparison details"):
        st.dataframe(comparison, use_container_width=True, hide_index=True)
