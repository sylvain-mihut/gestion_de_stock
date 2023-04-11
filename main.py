import mysql.connector
import tkinter as tk
from tkinter import ttk
# from crud_categorie import *
# from crud_produit import *
from connect import *

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

    # Création d'un widget Frame pour contenir le tableau
    table_frame = tk.Frame(root)
    table_frame.pack(fill='both', expand=True)

    # Création du tableau
    table = ttk.Treeview(table_frame, columns=columns, show='headings')
    
    for col in columns:
        table.heading(col, text=col)

    for row in rows:
        table.insert('', 'end', values=row)

    table.pack(side='left', fill='both', expand=True)

    

    # Fonction pour afficher les détails d'un article dans une nouvelle fenêtre
    def show_details(event):
        # Récupération de l'ID de l'article sélectionné
        item_id = table.selection()[0]
        item = table.item(item_id)['values'][0]

        # Connexion à la base de données
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="boutique"
        )

        cursor = conn.cursor()

        # Exécution d'une requête SQL pour récupérer les détails de l'article sélectionné
        cursor.execute('SELECT * FROM produit WHERE id=%s', (item,))

        # Récupération des résultats de la requête
        result = cursor.fetchone()

        # Création d'une nouvelle fenêtre pour afficher les détails de l'article
        details_window = tk.Toplevel(root)
        details_window.title('Détails de l\'article')
        details_window.geometry('400x400')

        # Création d'un widget Frame pour contenir les détails de l'article
        details_frame = tk.Frame(details_window)
        details_frame.pack(fill='both', expand=True)

        # Affichage des détails de l'article dans le widget Frame
        for i in range(len(columns)):
            label = tk.Label(details_frame, text=columns[i] + ':', font=('Arial', 12))
            label.grid(row=i, column=0, padx=5, pady=5, sticky='w')

            if i == 2:
                value = tk.Label(details_frame, text=result[i], font=('Arial', 12), wraplength=250, justify='left')
                value.grid(row=i, column=1, padx=5, pady=5, sticky='nsew')
            else:
                value = tk.Label(details_frame, text=result[i], font=('Arial', 12))
                value.grid(row=i, column=1, padx=5, pady=5, sticky='w')

        details_window.mainloop()

    table.bind('<ButtonRelease-1>', show_details)

    # Fermeture de la connexion à la base de données
    conn.close()

# Création de l'interface graphique
root = tk.Tk()
button = tk.Button(root, text='Produits', command=get_data)
button.pack()

# Lancement de l'interface graphique
root.mainloop()