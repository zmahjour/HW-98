from http.server import HTTPServer, BaseHTTPRequestHandler
from typing import Any
import requests
import datetime
import json
import urllib.parse
from database import WeatherDatabase


def get_response(city_name: str, API_key: str = "a2b998fddb840dbfc31ce7eca178d10e"):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric"
    response = requests.get(url)
    return response


def time_convert(dt: int) -> str:
    converted_dt = datetime.datetime.fromtimestamp(dt)
    str_dt = converted_dt.strftime("%Y-%m-%d %H:%M:%S")
    return str_dt


def get_city_weather(city_name: str) -> Any:
    response = get_response(city_name)
    if response.status_code == 200:
        data = response.json()
        dt = time_convert(data["dt"])
        weather_data = {
            "temp": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "last_updated_time": dt,
        }
    else:
        weather_data = {
            "temp": None,
            "feels_like": None,
            "last_updated_time": None,
        }
    return response, weather_data


host = "127.0.0.1"
port = 8080


class WeatherServer(BaseHTTPRequestHandler):
    @staticmethod
    def parse(url: str) -> str:
        parsed_url = urllib.parse.urlparse(url)
        query_params = urllib.parse.parse_qs(parsed_url.query)
        city_name = query_params.get("city")[0]
        return city_name

    def do_GET(self):
        city_name = WeatherServer.parse(self.path)
        WeatherDatabase.save_request_data(city_name)
        request_id = WeatherDatabase.get_request_id()
        response, weather_response = get_city_weather(city_name)
        if response.status_code == 200:
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            weather_data = json.dumps(weather_response).encode("utf-8")
            self.wfile.write(weather_data)

        elif response.status_code == 404:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            res = json.dumps(f"No matching location found; {weather_response}").encode(
                "utf-8"
            )
            self.wfile.write(res)

        else:
            self.send_response(response.status_code)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            res = json.dumps(f"Something was wrong; {weather_response}").encode("utf-8")
            self.wfile.write(res)

        WeatherDatabase.save_response_data(
            request_id,
            response.status_code,
            weather_response["temp"],
            weather_response["feels_like"],
            weather_response["last_updated_time"],
        )


server = HTTPServer((host, port), WeatherServer)
print("Weather Server running")

server.serve_forever()
server.server_close()
print("Server stopped")
