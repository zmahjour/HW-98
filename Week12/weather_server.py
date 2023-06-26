from http.server import HTTPServer, BaseHTTPRequestHandler
import requests
import datetime
import json


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

    else:
        return {}


host = "192.168.56.1"
port = 8080


class WeatherServer(BaseHTTPRequestHandler):
    def do_GEt(self):
        if weather_data:
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            weather_data = json.dumps(weather_data)
            self.wfile.write(bytes(weather_data, "utf-8"))

        else:
            self.send_response = 500


server = HTTPServer((host, port), WeatherServer)
print("Weather Server running")

server.serve_forever()
server.server_close()
print("Server stopped")
