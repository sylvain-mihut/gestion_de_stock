import mysql.connector

class CRUD_Categorie:
    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    
    def create(self, nom):
        cursor = self.db.cursor()
        sql = "INSERT INTO categorie (nom) VALUES (%s)"
        val = (nom)
        cursor.execute(sql, val)
        self.db.commit()
        return cursor.lastrowid
    
    def read(self, id):
        cursor = self.db.cursor()
        sql = "SELECT * FROM categorie WHERE id=%s"
        val = (id)
        cursor.execute(sql, val)
        return cursor.fetchone()
    
    def update(self, id, nom):
        cursor = self.db.cursor()
        sql = "UPDATE categorie SET nom=%s"
        val = (nom, id)
        cursor.execute(sql, val)
        self.db.commit()
    
    def delete(self, id):
        cursor = self.db.cursor()
        sql = "DELETE FROM categorie WHERE id=%s"
        val = (id,)
        cursor.execute(sql, val)
        self.db.commit()

    def list_all(self):
        cursor = self.db.cursor()
        sql = "SELECT * FROM categorie"
        cursor.execute(sql)
        return cursor.fetchall()


crud_Categorie = CRUD_Categorie("localhost", "root", "", "boutique")
