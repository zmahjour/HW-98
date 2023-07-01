import requests


def start_client():
    base_url = "http://127.0.0.1:8080/"
    city_name = input("Enter a city name: ")
    final_url = f"{base_url}?city={city_name}"
    response = requests.get(final_url)
    if response.status_code == 200:
        data = response.json()
        print(
            f"Temperature: {data['temp']}\nFells like: {data['feels_like']}\nLast updated: {data['last_updated_time']}\n"
        )
    else:
        print(response.json())
