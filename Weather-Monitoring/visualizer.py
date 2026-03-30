import matplotlib.pyplot as plt
from datetime import datetime
from .database import connect_db
from .config import CITIES

def plot_daily_trend(date):
    conn = connect_db()
    c = conn.cursor()

    start_of_day = int(datetime.combine(date, datetime.min.time()).timestamp())
    end_of_day = int(datetime.combine(date, datetime.max.time()).timestamp())

    for city in CITIES:
        c.execute('''SELECT temperature, timestamp FROM weather 
                     WHERE city = ? AND timestamp BETWEEN ? AND ?''', 
                     (city, start_of_day, end_of_day))
        results = c.fetchall()

        if results:
            temps = [r[0] for r in results]
            timestamps = [datetime.fromtimestamp(r[1]) for r in results]

            plt.plot(timestamps, temps, label=city)

    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.title(f"Temperature Trend on {date}")
    plt.legend()
    plt.show()

    conn.close()
