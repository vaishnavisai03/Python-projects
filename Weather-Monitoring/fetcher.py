from .api import fetch_weather
from .database import store_weather
from .config import CITIES

def fetch_and_store_weather():
    for city in CITIES:
        weather_data = fetch_weather(city)
        if weather_data:
            store_weather(weather_data)
    print("Data fetched and stored.")
