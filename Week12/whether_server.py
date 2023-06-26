import requests
import datetime


def get_city_weather(
    city_name: str, API_key: str = "a2b998fddb840dbfc31ce7eca178d10e"
) -> dict:
    url = (
        f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}"
    )
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        last_upadated_time = datetime.datetime.fromtimestamp(data["dt"])
        weather_data = {
            "temp": data["main"]["temp"],
            "feels like": data["main"]["feels_like"],
            "last updated time": last_upadated_time,
        }
        return weather_data
