import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

class DBManager:
    def __init__(self):
        self.conn = psycopg2.connect(
            host=os.getenv("FSTR_DB_HOST"),
            port=os.getenv("FSTR_DB_PORT"),
            user=os.getenv("FSTR_DB_LOGIN"),
            password=os.getenv("FSTR_DB_PASS"),
            database="fstr_db"
        )
        self.cursor = self.conn.cursor()

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params)
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def add_pass(self, name, description):
        query = "INSERT INTO passes (name, description) VALUES (%s, %s) RETURNING id;"
        self.cursor.execute(query, (name, description))
        pass_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return pass_id