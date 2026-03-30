from datetime import datetime
from .database import connect_db
from .config import CITIES
def calculate_daily_summary(date):
    conn = connect_db()
    c = conn.cursor()
    start_of_day = int(datetime.combine(date, datetime.min.time()).timestamp())
    end_of_day = int(datetime.combine(date, datetime.max.time()).timestamp())
    summaries = {}
    for city in CITIES:
        c.execute('''SELECT temperature, weather_main FROM weather 
                     WHERE city = ? AND timestamp BETWEEN ? AND ?''', 
                     (city, start_of_day, end_of_day))
        results = c.fetchall()
        if results:
            temps = [r[0] for r in results]
            weather_conditions = [r[1] for r in results]
            avg_temp = sum(temps) / len(temps)
            max_temp = max(temps)
            min_temp = min(temps)
            dominant_weather = max(set(weather_conditions), key=weather_conditions.count)
            summaries[city] = {
                'avg_temp': avg_temp,
                'max_temp': max_temp,
                'min_temp': min_temp,
                'dominant_weather': dominant_weather
            }
    conn.close()
    return summaries
