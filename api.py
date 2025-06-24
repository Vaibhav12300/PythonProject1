import requests
def weather(city):
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=fa2669bcb8b16879c63e73bc2c77c157&units=metric"
    try:
        response=requests.get(url)
        response.raise_for_status()
        data=response.json()

        temperature=data["main"]["temp"]
        humidity=data["main"]["humidity"]
        feels_like=data["main"]["feels_like"]
        print(f"weather in {city}:")
        print(f"temperature:{temperature}C(feels like:{feels_like}C")
        print(f"humidity:{humidity}%")
        print(f"description: {data["weather"][0]["description"].capitalize()}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data:{e}")
city=input("enter city name:")

weather(city)
