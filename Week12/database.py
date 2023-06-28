import psycopg2
from typing import List, Tuple, Any


class WeatherDatabase:
    @staticmethod
    def connect_to_db() -> Any:
        conn = psycopg2.connect(
            database="weather", user="postgres", password="13751375", port=5433
        )
        return conn

    @classmethod
    def create_request_table(cls) -> None:
        conn = WeatherDatabase.connect_to_db()
        with conn.cursor() as cur:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS request (
                request_id SERIAL PRIMARY KEY,
                city_name VARCHAR(50),
                request_time TIMESTAMP
                )
            """
            )
            conn.commit()
            conn.close()

    @classmethod
    def create_response_table(cls) -> None:
        conn = WeatherDatabase.connect_to_db()
        with conn.cursor() as cur:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS response (
                response_id SERIAL PRIMARY KEY,
                request_id REFERENCES request (request_id),
                response_time TIMESTAMP,
                status_code INTEGER,
                temperature REAL,
                feels_like REAL,
                last_updated VARCHAR(20)
                )
            """
            )
            conn.commit()
            conn.close()

    @classmethod
    def save_request_data(cls, city_name: str, request_time: str) -> None:
        conn = WeatherDatabase.connect_to_db()
        with conn.cursor() as cur:
            cur.execute(
                f"INSERT INTO request (city_name, request_time) VALUES ({city_name}, {request_time})"
            )
            conn.commit()
            conn.close()

    def save_response_data(self, city_name: str, response_data: dict) -> None:
        """
        Save response data for a city to the database.

        Args:
        - city_name (str): The name of the city to save response data for.
        - response_data (dict): A dictionary containing weather information for the city, including temperature, feels like temperature, and last updated time.

        Returns:
        - None
        """
        pass

    def get_request_count(self) -> int:
        """
        Get the total number of requests made to the server.

        Returns:
        - int: The total number of requests made to the server.
        """
        pass

    def get_successful_request_count(self) -> int:
        """
        Get the total number of successful requests made to the server.

        Returns:
        - int: The total number of successful requests made to the server.
        """
        pass

    def get_last_hour_requests(self) -> List[Tuple[str, str]]:
        """
        Get a list of requests made in the last hour.

        Returns:
        - List[Tuple[str, str]]: A list of tuples containing the name of the city and the time the request was made, in ISO format.
        """
        pass

    def get_city_request_count(self) -> List[Tuple[str, int]]:
        """
        Get a count of requests made for each city.

        Returns:
        - List[Tuple[str, int]]: A list of tuples containing the name of the city and the number of requests made for that city.
        """
        pass
