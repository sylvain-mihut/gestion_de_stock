import mysql.connector

class Connect:
    def init(self):
        self.conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="boutique"
        )
        self.cursor = self.conn.cursor()
