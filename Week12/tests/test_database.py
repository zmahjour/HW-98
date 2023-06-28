import unittest
from database import WeatherDatabase as wdb
import psycopg2


class WeatherDatabseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        conn = psycopg2.connect(
            database="postgres", user="postgres", password="13751375", port=5433
        )
        with conn.cursor() as cur:
            conn.autocommit = True
            cur.execute("CREATE DATABASE t_weather")
        conn.close()
        # cls.conn = psycopg2.connect(
        #     database="t_weather", user="postgres", password="13751375", port=5433
        # )
        # cls.cur = cls.conn.cursor()

    @classmethod
    def tearDownClass(cls):
        # cls.cur.close()
        # cls.conn.close()
        conn = psycopg2.connect(
            database="postgres", user="postgres", password="13751375", port=5433
        )
        with conn.cursor() as cur:
            conn.autocommit = True
            cur.execute("DROP DATABASE t_weather")
        conn.close()

    def test_connect_to_db(self):
        conn = wdb.connect_to_db(
            database="postgres", user="postgres", password="13751375", port=5433
        )
        self.assertIs(type(conn), psycopg2.extensions.connection)

    def test_create_request_table(self):
        # wdb.create_request_table(
        #     database="t_weather", user="postgres", password="13751375", port=5433
        # )
        # conn = psycopg2.connect(database="t_weather")
        # with conn.cursor() as cur:
        pass

    def test_create_response_table(self):
        pass

    def test_save_request_data(self):
        wdb.save_request_data(
            city_name="Tehran",
            database="t_weather",
            user="postgres",
            password="13751375",
            port=5433,
        )
        with psycopg2.connect(
            database="t_weather", user="postgres", password="13751375", port=5433
        ) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                CREATE TABLE IF NOT EXISTS request (
                request_id SERIAL PRIMARY KEY,
                city_name VARCHAR(50),
                request_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )"""
                )
                conn.commit()
                cur.execute(
                    "SELECT city_name FROM request ORDER BY request_id DESC LIMIT 1"
                )
                result = cur.fetchall()
        self.assertEqual(result[0], "Tehran")

    def test_save_response_data(self):
        pass

    def test_get_request_id(self):
        pass

    def test_get_request_count(self):
        pass

    def test_get_successful_request_count(self):
        pass

    def test_get_last_hour_requests(self):
        pass

    def test_get_city_request_count(self):
        pass


if __name__ == "__main__":
    unittest.main()
