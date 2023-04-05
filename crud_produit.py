import mysql.connector

class CRUD_Produit:
    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    
    def create(self, nom, description, prix, quantite, id_categorie):
        cursor = self.db.cursor()
        sql = "INSERT INTO produit (nom, description, prix, quantite, id_categorie) VALUES (%s, %s, %s, %s, %s)"
        val = (nom, description, prix, quantite, id_categorie)
        cursor.execute(sql, val)
        self.db.commit()
        return cursor.lastrowid
    
    def read(self, id):
        cursor = self.db.cursor()
        sql = "SELECT * FROM produit WHERE id=%s"
        val = (id,)
        cursor.execute(sql, val)
        return cursor.fetchone()
    
    def update(self, id, nom, description, prix, quantite, id_categorie):
        cursor = self.db.cursor()
        sql = "UPDATE produit SET nom=%s, description=%s, prix=%s, quantite=%s, id_categorie=%s WHERE id=%s"
        val = (nom, description, prix, quantite, id_categorie, id)
        cursor.execute(sql, val)
        self.db.commit()
    
    def delete(self, id):
        cursor = self.db.cursor()
        sql = "DELETE FROM produit WHERE id=%s"
        val = (id,)
        cursor.execute(sql, val)
        self.db.commit()

    def list_all(self):
        cursor = self.db.cursor()
        sql = "SELECT * FROM produit"
        cursor.execute(sql)
        return cursor.fetchall()

crud_Produit = CRUD_Produit("localhost", "root", "", "boutique")
