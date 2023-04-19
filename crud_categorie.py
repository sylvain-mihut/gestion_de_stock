import mysql.connector
from Connect import *

class CRUD_Categorie(Connect):
    def __init__(self):
        super().__init__()
    
    def create(self, nom):
        sql = "INSERT INTO categorie (nom) VALUES (%s)"
        val = (nom)
        self.cursor.execute(sql, val)
        self.conn.commit()
        return self.cursor.lastrowid
    
    def read(self, id):
        sql = "SELECT * FROM categorie WHERE id=%s"
        val = (id)
        self.cursor.execute(sql, val)
        return self.cursor.fetchone()
    
    def update(self, id, nom):
        sql = "UPDATE categorie SET nom=%s"
        val = (nom, id)
        self.cursor.execute(sql, val)
        self.conn.commit()
    
    def delete(self, id):
        sql = "DELETE FROM categorie WHERE id=%s"
        val = (id,)
        self.cursor.execute(sql, val)
        self.conn.commit()

    def list_all(self):
        sql = "SELECT * FROM categorie"
        self.cursor.execute(sql)
        return self.cursor.fetchall()


