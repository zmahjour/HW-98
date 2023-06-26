import requests


base_url = "http://127.0.0.1:8080/"
city_name = input("Enter a city name: ")
final_url = f"{base_url}?city={city_name}"

response = requests.get(final_url)
print(response.json())
