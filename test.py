import mysql.connector
import tkinter as tk
from tkinter import ttk

# Fonction pour récupérer les données de la base de données et les afficher dans l'interface graphique
def get_data():
    # Connexion à la base de données
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="boutique"
    )

    cursor = conn.cursor()

    # Exécution d'une requête SQL pour récupérer les données
    cursor.execute('SELECT * FROM produit')

    # Création d'un tableau pour afficher les résultats de la requête
    columns = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()

    table = ttk.Treeview(root, columns=columns, show='headings')
    for col in columns:
        table.heading(col, text=col)

    for row in rows:
        table.insert('', 'end', values=row)

    table.pack()

    # Fermeture de la connexion à la base de données
    conn.close()

# Création de l'interface graphique
root = tk.Tk()
button = tk.Button(root, text='Get Data', command=get_data)
button.pack()

# Lancement de l'interface graphique
root.mainloop()
