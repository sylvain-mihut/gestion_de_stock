import mysql.connector
from Connect import *

class CRUD_Produit(Connect):
    def __init__(self):
        super().__init__()
    
    def create(self, nom, description, prix, quantite, id_categorie):
        sql = "INSERT INTO produit (nom, description, prix, quantite, id_categorie) VALUES (%s, %s, %s, %s, %s)"
        val = (nom, description, prix, quantite, id_categorie)
        self.cursor.execute(sql, val)
        self.conn.commit()
    
    def read(self, id):
        sql = "SELECT * FROM produit WHERE id=%s"
        val = (id,)
        self.cursor.execute(sql, val)
        return self.cursor.fetchone()
    
    def update(self, id, nom, description, prix, quantite, id_categorie):
        sql = "UPDATE produit SET nom=%s, description=%s, prix=%s, quantite=%s, id_categorie=%s WHERE id=%s"
        val = (nom, description, prix, quantite, id_categorie, id)
        self.cursor.execute(sql, val)
        self.conn.commit()
    
    def delete(self, id):
        sql = "DELETE FROM produit WHERE id=%s"
        val = (id,)
        self.cursor.execute(sql, val)
        self.conn.commit()

    def list_all(self):
        sql = "SELECT * FROM produit"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

