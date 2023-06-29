import psycopg2
from typing import List, Tuple, Any


class WeatherDatabase:
    @staticmethod
    def connect_to_db(
        database="weather", user="postgres", password="13751375", port=5433
    ):
        conn = psycopg2.connect(
            database=database, user=user, password=password, port=port
        )
        return conn

    @classmethod
    def create_request_table(
        cls, database="weather", user="postgres", password="13751375", port=5433
    ) -> None:
        conn = cls.connect_to_db(
            database=database, user=user, password=password, port=port
        )
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
    def create_response_table(
        cls, database="weather", user="postgres", password="13751375", port=5433
    ) -> None:
        conn = cls.connect_to_db(
            database=database, user=user, password=password, port=port
        )
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
    def save_request_data(
        cls,
        city_name: str,
        database="weather",
        user="postgres",
        password="13751375",
        port=5433,
    ) -> None:
        conn = cls.connect_to_db(
            database=database, user=user, password=password, port=port
        )
        with conn.cursor() as cur:
            cur.execute(f"INSERT INTO request (city_name) VALUES ('{city_name}')")
            conn.commit()
        conn.close()

    @classmethod
    def save_response_data(
        cls,
        request_id,
        status_code,
        temperature,
        feels_like,
        last_updated,
        database="weather",
        user="postgres",
        password="13751375",
        port=5433,
    ) -> None:
        values = (request_id, status_code, temperature, feels_like, last_updated)
        conn = cls.connect_to_db(
            database=database, user=user, password=password, port=port
        )
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO response (request_id, status_code, temperature, feels_like, last_updated) VALUES (%s, %s, %s, %s, %s)",
                values,
            )
            conn.commit()
        conn.close()

    @classmethod
    def get_request_id(
        cls, database="weather", user="postgres", password="13751375", port=5433
    ) -> int:
        conn = cls.connect_to_db(
            database=database, user=user, password=password, port=port
        )
        with conn.cursor() as cur:
            cur.execute(
                f"SELECT request_id FROM request ORDER BY request_id DESC LIMIT 1"
            )
            row = cur.fetchall()
        conn.close()
        return row[0][0]

    @classmethod
    def get_request_count(
        cls, database="weather", user="postgres", password="13751375", port=5433
    ) -> int:
        conn = cls.connect_to_db(
            database=database, user=user, password=password, port=port
        )
        with conn.cursor() as cur:
            cur.execute(f"SELECT COUNT(*) FROM request")
            row = cur.fetchall()
        conn.close()
        print(f"Total number of requests: {row[0][0]}")
        return row[0][0]

    @classmethod
    def get_successful_request_count(
        cls, database="weather", user="postgres", password="13751375", port=5433
    ) -> int:
        conn = cls.connect_to_db(
            database=database, user=user, password=password, port=port
        )
        with conn.cursor() as cur:
            cur.execute(f"SELECT COUNT(*) FROM response WHERE status_code = 200")
            row = cur.fetchall()
        conn.close()
        print(f"Total number of successful requests: {row[0][0]}")

    @classmethod
    def get_last_hour_requests(
        cls, database="weather", user="postgres", password="13751375", port=5433
    ) -> List[Tuple[str, str]]:
        conn = cls.connect_to_db(
            database=database, user=user, password=password, port=port
        )
        with conn.cursor() as cur:
            cur.execute(
                f"SELECT city_name, request_time FROM request WHERE request_time >= CURRENT_TIMESTAMP - INTERVAL '1 hour'"
            )
            rows = cur.fetchall()
        conn.close()
        for row in rows:
            print(f"{row[0]}: {row[1]}")

    @classmethod
    def get_city_request_count(
        cls, database="weather", user="postgres", password="13751375", port=5433
    ) -> List[Tuple[str, int]]:
        conn = cls.connect_to_db(
            database=database, user=user, password=password, port=port
        )
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT LOWER(city_name) as city_name, COUNT(*) AS number_of_requests
                FROM request
                JOIN response ON response.request_id = request.request_id
                WHERE status_code = 200
                GROUP BY LOWER(city_name)
            """
            )
            rows = cur.fetchall()
        conn.close()
        for row in rows:
            print(f"{row[0]}: {row[1]}")
        return rows


WeatherDatabase.create_request_table()
WeatherDatabase.create_response_table()
