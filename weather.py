# weather.py
import requests

def get_weather(API_KEY, CITY):
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}"
    try:
        response = requests.get(url)
        data = response.json()
        if "error" in data:
            return None
        else:
            weather_info = {
                "temperature": data["current"]["temp_c"],
                "description": data["current"]["condition"]["text"]
            }
            return weather_info
    except Exception as e:
        print(f"Error fetching weather information: {e}")
        return None
