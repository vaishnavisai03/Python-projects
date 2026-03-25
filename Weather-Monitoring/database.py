import sqlite3

DB_NAME = 'weather_data.db'

def connect_db():
    conn = sqlite3.connect(DB_NAME)
    return conn

def create_tables():
    conn = connect_db()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS weather (
                    city TEXT, 
                    timestamp INTEGER, 
                    temperature REAL, 
                    feels_like REAL, 
                    weather_main TEXT)''')
    conn.commit()
    conn.close()

def store_weather(data):
    conn = connect_db()
    c = conn.cursor()
    c.execute('''INSERT INTO weather (city, timestamp, temperature, feels_like, weather_main) 
                 VALUES (?, ?, ?, ?, ?)''', 
                 (data['city'], data['timestamp'], data['temperature'], 
                  data['feels_like'], data['weather_main']))
    conn.commit()
    conn.close()
