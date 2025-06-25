import csv
import sqlite3
import pandas as pd

address_book = [
    ["Name", "Address", "Mobile", "Email"],
    ["VG", "123 Main Street", "9876543210", "vg@example.com"],
    ["DJ", "456 Maple Avenue", "9123456780", "dj@example.com"],
    ["LJ Johnson", "789 Oak Drive", "9988776655", "lj@example.com"]
]

with open("address_book.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(address_book)

print(" Address Book CSV created!")


#----------------------------------------------------------------------------
import requests
from datetime import datetime

def weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=fa2669bcb8b16879c63e73bc2c77c157&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data["cod"] != 200:
            print("City not found. Please check the spelling.")
            return
        city_name = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        min_temp = data["main"]["temp_min"]
        max_temp = data["main"]["temp_max"]
        wind_speed = data["wind"]["speed"]
        description = data["weather"][0]["description"].capitalize()
        sunrise = datetime.fromtimestamp(data["sys"]["sunrise"]).strftime('%H:%M:%S')
        sunset = datetime.fromtimestamp(data["sys"]["sunset"]).strftime('%H:%M:%S')
        print("\n" + "=" * 40)
        print(f" Weather Report for {city_name}, {country}")
        print("=" * 40)
        print(f" Temperature     : {temperature}°C (Feels like {feels_like}°C)")
        print(f" Min Temp        : {min_temp}°C")
        print(f" Max Temp        : {max_temp}°C")
        print(f" Humidity        : {humidity}%")
        print(f"Wind Speed      : {wind_speed} m/s")
        print(f" Sunrise         : {sunrise}")
        print(f" Sunset          : {sunset}")
        print(f" Description     : {description}")
        print("=" * 40 + "\n")

    except requests.exceptions.RequestException as e:
        print(f" Error fetching weather data: {e}")
    except KeyError:
        print(" Error: Unexpected response format.")
while True:
    city = input("Enter city name (or type 'exit' to quit): ")
    if city.strip().lower() == 'exit':
        print("Goodbye! ")
        break
    elif city.strip() == "":
        print("Please enter a valid city name.")
    else:
        weather(city)

#----------------------------------------------------------------------------------
conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
cursor.execute("CREATE TABLE IF NOT EXISTS courses (id INTEGER PRIMARY KEY, course_name TEXT, credits INTEGER)")

cursor.execute("INSERT INTO students (name, age) VALUES ('Alice', 20)")
cursor.execute("INSERT INTO students (name, age) VALUES ('Bob', 22)")
cursor.execute("INSERT INTO courses (course_name, credits) VALUES ('Math', 4)")
cursor.execute("INSERT INTO courses (course_name, credits) VALUES ('Science', 3)")

conn.commit()

print("\n Students:")
for row in cursor.execute("SELECT * FROM students"):
    print(row)

print("\n Courses:")
for row in cursor.execute("SELECT * FROM courses"):
    print(row)

cursor.execute("UPDATE students SET age = 21 WHERE name = 'Alice'")
conn.commit()

cursor.execute("DELETE FROM courses WHERE course_name = 'Science'")
conn.commit()

print("\nUpdated Students Table:")
for row in cursor.execute("SELECT * FROM students"):
    print(row)

print("\nCourses Table after Deletion:")
for row in cursor.execute("SELECT * FROM courses"):
    print(row)
conn.close()