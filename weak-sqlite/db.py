import sqlite3

class Database:
    def __init__(self, dbcredits: str) -> None:
        self.connection = sqlite3.connect('db.db', check_same_thread=False)
        self.cursor = self.connection.cursor()
    def check_credentials(self, login: str, password: str) -> bool:
        q = f"""SELECT * FROM credits WHERE login = '{login}' AND password = '{password}'"""
        print(q)
        result = self.cursor.execute(q).fetchone()
        return bool(result)