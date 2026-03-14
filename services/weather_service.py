# services/weather_service.py

import requests


API_KEY = "YOUR_OPENWEATHER_API_KEY"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(latitude, longitude):

    try:

        params = {
            "lat": latitude,
            "lon": longitude,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(BASE_URL, params=params, timeout=10)

        if response.status_code != 200:
            return {"error": "Weather API request failed"}

        data = response.json()

        weather_data = {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "condition": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"]
        }

        return weather_data

    except Exception as e:

        return {
            "error": str(e)
        }