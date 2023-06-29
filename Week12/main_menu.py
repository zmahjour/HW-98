from menu.models import generate_menu_from_dict
from weather_client import start_client
from database import WeatherDatabase

main_menu_dict = {
    "name": "Weather Menu",
    "children": [
        {
            "name": "Weather in your city",
            "action": start_client,
        },
        {
            "name": "Total number of requests",
            "action": WeatherDatabase.get_request_count,
        },
        {
            "name": "Total number of successful requests",
            "action": WeatherDatabase.get_successful_request_count,
        },
        {
            "name": "Last hour requests",
            "action": WeatherDatabase.get_last_hour_requests,
        },
        {
            "name": "Count of requests for each city",
            "action": WeatherDatabase.get_city_request_count,
        },
    ],
}


def menu_run():
    menu = generate_menu_from_dict(main_menu_dict, parent=None)
    menu()
