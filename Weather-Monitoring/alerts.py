
from .database import connect_db
from .config import ALERT_THRESHOLD_TEMP

def check_alerts():
    conn = connect_db()
    c = conn.cursor()
    c.execute('''SELECT city, temperature, weather_main, timestamp 
                 FROM weather ORDER BY timestamp DESC LIMIT 6''')
    latest_data = c.fetchall()
    
    for data in latest_data:
        city, temperature, weather_main, timestamp = data
        if temperature > ALERT_THRESHOLD_TEMP:
            print(f"ALERT: {city} exceeded {ALERT_THRESHOLD_TEMP}°C with {temperature}°C")
    
    conn.close()
