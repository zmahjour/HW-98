import unittest
from database import WeatherDatabase as wdb
import psycopg2


class WeatherDatabseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        conn = wdb.connect_to_db(database="postgres")
        with conn.cursor() as cur:
            conn.autocommit = True
            cur.execute("CREATE DATABASE t_weather")
        conn.close()
        cls.conn = wdb.connect_to_db(database="t_weather")
        cls.cur = cls.conn.cursor()

    def setUp(self):
        self.create_req_table_command = """
            CREATE TABLE IF NOT EXISTS request (
            request_id SERIAL PRIMARY KEY,
            city_name VARCHAR(50),
            request_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
        """
        self.create_res_table_command = """
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

    def tearDown(self):
        self.cur.execute("DROP TABLE IF EXISTS response")
        self.cur.execute("DROP TABLE IF EXISTS request")
        self.conn.commit()

    @classmethod
    def tearDownClass(cls):
        cls.cur.close()
        cls.conn.close()
        conn = wdb.connect_to_db(database="postgres")
        with conn.cursor() as cur:
            conn.autocommit = True
            cur.execute("DROP DATABASE t_weather")
        conn.close()

    def test_connect_to_db(self):
        conn = wdb.connect_to_db(database="postgres")
        self.assertIs(type(conn), psycopg2.extensions.connection)

    def test_create_request_table(self):
        wdb.create_request_table(database="t_weather")
        self.cur.execute(
            "SELECT EXISTS(SELECT 1 FROM information_schema.tables WHERE table_name = 'request')"
        )
        table_exists = self.cur.fetchone()[0]
        self.assertTrue(table_exists)

    def test_create_response_table(self):
        self.cur.execute(self.create_req_table_command)
        self.conn.commit()
        wdb.create_response_table(database="t_weather")
        self.cur.execute(
            "SELECT EXISTS(SELECT 1 FROM information_schema.tables WHERE table_name = 'response')"
        )
        table_exists = self.cur.fetchone()[0]
        self.assertTrue(table_exists)

    def test_save_request_data(self):
        self.cur.execute(self.create_req_table_command)
        self.conn.commit()
        wdb.save_request_data(city_name="Tehran", database="t_weather")
        self.cur.execute("SELECT city_name FROM request")
        result = self.cur.fetchall()
        self.assertEqual(result[0][0], "Tehran")

    def test_save_response_data(self):
        self.cur.execute(self.create_req_table_command)
        self.cur.execute("INSERT INTO request (city_name) VALUES ('Tehran')")
        self.cur.execute(self.create_res_table_command)
        self.conn.commit()
        wdb.save_response_data(
            request_id=1,
            status_code=200,
            temperature=30,
            feels_like=27,
            last_updated="2023-6-29 12:00:00",
            database="t_weather",
        )
        self.cur.execute(
            "SELECT request_id, status_code, temperature, feels_like, last_updated FROM response"
        )
        result = self.cur.fetchall()
        self.assertEqual(result[0], (1, 200, 30, 27, "2023-6-29 12:00:00"))

    def test_get_request_id(self):
        self.cur.execute(self.create_req_table_command)
        self.cur.execute("INSERT INTO request (city_name) VALUES ('Tehran')")
        self.conn.commit()
        result = wdb.get_request_id(database="t_weather")
        self.assertEqual(result, 1)

    def test_get_request_count(self):
        self.cur.execute(self.create_req_table_command)
        self.cur.execute("INSERT INTO request (city_name) VALUES ('Tehran')")
        self.cur.execute("INSERT INTO request (city_name) VALUES ('Shiraz')")
        self.cur.execute("INSERT INTO request (city_name) VALUES ('Wien')")
        self.conn.commit()
        result = wdb.get_request_count(database="t_weather")
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
