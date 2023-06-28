import psycopg2
from typing import List, Tuple, Any


class WeatherDatabase:
    @staticmethod
    def connect_to_db():
        conn = psycopg2.connect(
            database="weather", user="postgres", password="13751375", port=5433
        )
        return conn

    @classmethod
    def create_request_table(cls) -> None:
        conn = cls.connect_to_db()
        with conn.cursor() as cur:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS request (
                request_id SERIAL PRIMARY KEY,
                city_name VARCHAR(50),
                request_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """
            )
            conn.commit()
        conn.close()

    @classmethod
    def create_response_table(cls) -> None:
        conn = cls.connect_to_db()
        with conn.cursor() as cur:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS response (
                response_id SERIAL PRIMARY KEY,
                request_id INTEGER REFERENCES request (request_id) UNIQUE NOT NULL,
                response_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
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
    def save_request_data(cls, city_name: str) -> None:
        conn = cls.connect_to_db()
        with conn.cursor() as cur:
            cur.execute(f"INSERT INTO request (city_name) VALUES ('{city_name}')")
            conn.commit()
        conn.close()

    @classmethod
    def save_response_data(
        cls, request_id, status_code, temperature, feels_like, last_updated
    ) -> None:
        values = (request_id, status_code, temperature, feels_like, last_updated)
        conn = cls.connect_to_db()
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO response (request_id, status_code, temperature, feels_like, last_updated) VALUES (%s, %s, %s, %s, %s)",
                values,
            )
            conn.commit()
        conn.close()

    @classmethod
    def get_request_id(cls) -> int:
        conn = cls.connect_to_db()
        with conn.cursor() as cur:
            cur.execute(
                f"SELECT request_id FROM request ORDER BY request_id DESC LIMIT 1"
            )
            row = cur.fetchall()
        conn.close()
        return row[0]

    @classmethod
    def get_request_count(cls) -> int:
        conn = cls.connect_to_db()
        with conn.cursor() as cur:
            cur.execute(f"SELECT COUNT(*) FROM request")
            row = cur.fetchall()
        conn.close()
        return row[0]

    @classmethod
    def get_successful_request_count(cls) -> int:
        conn = cls.connect_to_db()
        with conn.cursor() as cur:
            cur.execute(f"SELECT COUNT(*) FROM response WHERE status_code = 200")
            row = cur.fetchall()
        conn.close()
        return row[0]

    @classmethod
    def get_last_hour_requests(cls) -> List[Tuple[str, str]]:
        conn = cls.connect_to_db()
        with conn.cursor() as cur:
            cur.execute(
                f"SELECT city_name, request_time FROM request WHERE request_time >= CURRENT_TIMESTAMP - INTERVAL '1 hour'"
            )
            rows = cur.fetchall()
        conn.close()
        return rows

    @classmethod
    def get_city_request_count(cls) -> List[Tuple[str, int]]:
        conn = cls.connect_to_db()
        with conn.cursor() as cur:
            cur.execute(
                f"SELECT city_name, COUNT(*) AS number_of_requests FROM request GROUP BY city_name"
            )
            rows = cur.fetchall()
        conn.close()
        return rows


WeatherDatabase.create_request_table()
WeatherDatabase.create_response_table()
