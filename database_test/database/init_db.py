import psycopg2

from config import (DB_USER,
                    DB_PASS,
                    DB_HOST,
                    DB_NAME)


class DatabaseConnection:
    """Подключение к базе данных."""

    def __init__(self, db_name, db_user, db_password, db_host):
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password
        self.db_host = db_host

    def get_connection(self):
        conn = psycopg2.connect(dbname=self.db_name,
                                user=self.db_user,
                                password=self.db_password,
                                host=self.db_host)
        conn.autocommit = True
        cursor = conn.cursor()
        return cursor


create = DatabaseConnection(DB_NAME,
                            DB_USER,
                            DB_PASS,
                            DB_HOST)
