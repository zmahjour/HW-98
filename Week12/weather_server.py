from http.server import HTTPServer, BaseHTTPRequestHandler
import requests
import datetime
import json
import urllib.parse


def get_city_weather(
    city_name: str, API_key: str = "a2b998fddb840dbfc31ce7eca178d10e"
) -> dict:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        dt = datetime.datetime.fromtimestamp(data["dt"])
        dt_str = dt.strftime("%Y-%m-%d %H:%M:%S")

        weather_data = {
            "temp": data["main"]["temp"],
            "feels like": data["main"]["feels_like"],
            "last updated time": dt_str,
        }
        return weather_data

    else:
        return {}


host = "127.0.0.1"
port = 8080


class WeatherServer(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_url.query)
        city_name = query_params.get("city")[0]
        print(city_name)
        weather_data = get_city_weather(city_name)
        if weather_data:
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            weather_data = json.dumps(weather_data).encode("utf-8")
            self.wfile.write(weather_data)

        else:
            self.send_response(404)


server = HTTPServer((host, port), WeatherServer)
print("Weather Server running")

server.serve_forever()
server.server_close()
print("Server stopped")
