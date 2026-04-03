# 🌦️ Weather Monitoring & Analytics System

A modular Python-based weather monitoring system that collects real-time weather data, stores it in a database, performs analysis, generates insights, and triggers alerts based on temperature thresholds.

---

## 🚀 Features

- Fetches real-time weather data using OpenWeather API  
- Stores data in SQLite database  
- Supports multiple cities monitoring  
- Generates daily summaries (average, max, min temperature)  
- Detects dominant weather conditions  
- Triggers alerts when temperature exceeds threshold  
- Visualizes temperature trends using graphs  

---

## 🛠️ Tech Stack

- Python  
- Requests (API calls)  
- SQLite (Database)  
- Matplotlib (Visualization)  

---

## 📂 Project Structure

Weather-Monitoring/

├── api.py          → Fetch weather data from API  
├── config.py       → API key, cities, thresholds  
├── database.py     → Database connection & storage  
├── fetcher.py      → Fetch + store pipeline  
├── alerts.py       → Temperature alert system  
├── rollups.py      → Daily summary calculations  
├── visualizer.py   → Graph plotting  

---

## ⚙️ Workflow

1. Fetch weather data for configured cities  
2. Store data in SQLite database  
3. Retrieve latest data for analysis  
4. Generate daily summaries (avg, max, min)  
5. Detect dominant weather condition  
6. Trigger alerts if threshold exceeded  
7. Visualize temperature trends  

---

## 📊 Example Functionality

- Tracks cities like Delhi, Mumbai, Chennai, Hyderabad  
- Converts temperature from Kelvin to Celsius  
- Alerts when temperature > 35°C  
- Plots time vs temperature graphs  

---

## 🔧 Setup & Installation

pip install requests matplotlib

---

## 🔑 Configuration

Update your API key in config.py:

API_KEY = "your_api_key_here"

You can also modify:
- Cities list  
- Temperature threshold  

---

## ▶️ Run Project

python fetcher.py

(Optional)

python visualizer.py  
python alerts.py  

---

## 📌 Future Improvements

- Add Streamlit dashboard  
- Automate scheduling (cron jobs)  
- Add ML-based prediction  
- Deploy on cloud  

---

## 🎯 Use Cases

- Real-time weather monitoring  
- Data analysis and visualization  
- Alert systems for extreme conditions  
- Foundation for ML-based forecasting
