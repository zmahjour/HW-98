import unittest
from weather_server import get_city_weather


class GetCityWeatherTest(unittest.TestCase):
    def test_get_city_weather(self):
        response_1, weather_data_1 = get_city_weather("Tehran")
        self.assertEqual(response_1.status_code, 200)
        self.assertIsNotNone(weather_data_1["temp"])
        self.assertIsNotNone(weather_data_1["feels_like"])
        self.assertIsNotNone(weather_data_1["last_updated_time"])

        response_2, weather_data_2 = get_city_weather("abc")
        self.assertEqual(response_2.status_code, 404)
        self.assertIsNone(weather_data_2["temp"])
        self.assertIsNone(weather_data_2["feels_like"])
        self.assertIsNone(weather_data_2["last_updated_time"])


if __name__ == "__main__":
    unittest.main()
