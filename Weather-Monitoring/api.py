import requests
from .config import API_KEY, BASE_URL

def fetch_weather(city):
    params = {'q': city, 'appid': API_KEY}
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return {
            'city': city,
            'temperature': data['main']['temp'] - 273.15,  # Kelvin to Celsius
            'feels_like': data['main']['feels_like'] - 273.15,
            'weather_main': data['weather'][0]['main'],
            'timestamp': data['dt']
        }
    else:
        print(f"Error fetching weather data for {city}: {response.status_code}")
        return None
