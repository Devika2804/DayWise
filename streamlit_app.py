import streamlit as st

# -----------------------------
# Components
# -----------------------------
from components.home import render_home
from components.insights import render_insights
from components.about import render_about

# -----------------------------
# Utilities
# -----------------------------
from utils.styles import load_css


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="DayWise",
    page_icon="🌤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
load_css()


# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.title("🌤️ DayWise")
    st.caption("Plan your day with AI-powered weather insights")

    st.markdown("")

    city = st.selectbox(
        "Select City",
        [
            "Bengaluru",
            "Chennai",
            "Coimbatore",
            "Hyderabad",
            "Mumbai"
        ],
        index=0
    )


# -----------------------------
# Navigation
# -----------------------------
page = st.segmented_control(
    "",
    [
        "🏠 Home",
        "📈 Insights",
        "💡 About"
    ],
    default="🏠 Home"
)


# -----------------------------
# Route Pages
# -----------------------------
if page == "🏠 Home":
    render_home(city)

elif page == "📈 Insights":
    render_insights(city)

elif page == "ℹ️ About":
    render_about()