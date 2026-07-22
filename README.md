# 🌤️ DayWise

DayWise is an AI-powered lifestyle dashboard built with Streamlit. It combines live weather, air quality, historical insights, and AI-generated recommendations to help users plan their day.

---

## ✨ Features

- 🌤️ Live Weather Information
- 🌫️ Air Quality Index (AQI)
- 🤖 AI Daily Brief using Google Gemini
- 🏆 Comfort Score
- 🚶 Walking Recommendation
- ⏰ Best Outdoor Time
- 🎒 Things to Carry
- 🍲 Food Suggestions
- ❤️ Health Tips
- 📈 Historical Weather & AQI Insights
- 🌍 City Comparison Dashboard

---

## 🛠️ Tech Stack

- Python
- Streamlit
- PostgreSQL
- Plotly
- Google Gemini API
- OpenWeather API
- AQI API

---

## 📂 Project Structure

```
DayWise/
│
├── assets/
├── components/
├── database/
├── modules/
├── utils/
│
├── streamlit_app.py
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/DayWise.git
```

Move into the project folder

```bash
cd DayWise
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment

### Windows

```bash
.venv\Scripts\activate
```

### macOS/Linux

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your API keys and database credentials.

Run the application

```bash
streamlit run streamlit_app.py
```

---

## 🔑 Environment Variables

Create a `.env` file with the following variables:

```env
OPENWEATHER_API_KEY=your_api_key
GEMINI_API_KEY=your_api_key

DB_HOST=your_host
DB_PORT=5432
DB_NAME=your_database
DB_USER=your_username
DB_PASSWORD=your_password
```

## 📄 License

This project is developed for learning and portfolio purposes.
