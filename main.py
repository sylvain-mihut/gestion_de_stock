import mysql.connector
import tkinter as tk
from tkinter import ttk
from CRUD_Categorie import *
from CRUD_Produit import *
from Connect import *

root = tk.Tk()
connect = Connect()
crud_product = CRUD_Produit()
crud_categories = CRUD_Categorie()
categories = crud_categories.list_all()
categories_names = [cat[1] for cat in categories]

# Fonction pour récupérer les données de la base de données et les afficher dans l'interface graphique
def get_data():

    for widget in root.winfo_children():
        widget.destroy()

    rows = crud_product.list_all()
    columns = [desc[0] for desc in crud_product.cursor.description]

    table_frame = tk.Frame(root)
    table_frame.pack(fill='both', expand=True)

    table = ttk.Treeview(table_frame, columns=columns, show='headings')
    
    for col in columns:
        table.heading(col, text=col)

    for row in rows:
        table.insert('', 'end', values=row)

    table.pack(side='left', fill='both', expand=True)
    button1 = tk.Button(root, text="Ajouté un produit", command=add_product)
    button1.pack(side=tk.BOTTOM)

    
    def show_details(event):
        item_id = table.selection()[0]
        item = table.item(item_id)['values'][0]

        result = crud_product.read(item)

        details_window = tk.Toplevel(root)
        details_window.title('Détails de l\'article')
        details_window.geometry('400x400')

        details_frame = tk.Frame(details_window)
        details_frame.pack(fill='both', expand=True)

        for i in range(len(columns)):
            label = tk.Label(details_frame, text=columns[i] + ':', font=('Arial', 12))
            label.grid(row=i, column=0, padx=5, pady=5, sticky='w')

            if i == 2:
                value = tk.Label(details_frame, text=result[i], font=('Arial', 12), wraplength=250, justify='left')
                value.grid(row=i, column=1, padx=5, pady=5, sticky='nsew')
            else:
                value = tk.Label(details_frame, text=result[i], font=('Arial', 12))
                value.grid(row=i, column=1, padx=5, pady=5, sticky='w')

        button2 = tk.Button(details_window, text="Modifié un produit", command=lambda product=result: modify_product(product))
        button3 = tk.Button(details_window, text="Supprimé un produit", command=lambda product=result: delete_product(product))
        button2.pack(side=tk.LEFT)
        button3.pack(side=tk.RIGHT)


        details_window.mainloop()

    table.bind('<ButtonRelease-1>', show_details)

def delete_product(product):
    crud_product.delete(product[0])
    get_data()

def modify_product(product):
    global categories_names
    add_window = tk.Toplevel(root)
    add_window.geometry("400x400")
    add_window.title("Modifier un produit")

    label_name = tk.Label(add_window, text="Nom")
    label_name.pack()
    entry_name = tk.Entry(add_window)
    entry_name.pack()
    entry_name.insert(0, product[1])

    label_description = tk.Label(add_window, text="Description")
    label_description.pack()
    entry_description = tk.Entry(add_window)
    entry_description.pack()
    entry_description.insert(0, product[2])

    label_price = tk.Label(add_window, text="Prix en €")
    label_price.pack()
    entry_price = tk.Entry(add_window)
    entry_price.pack()
    entry_price.insert(0, product[3])

    label_quantity = tk.Label(add_window, text="Quantité")
    label_quantity.pack()
    entry_quantity = tk.Entry(add_window)
    entry_quantity.pack()
    entry_quantity.insert(0, product[4])

    label_category = tk.Label(add_window, text="Catégorie")
    label_category.pack()
    category_var = tk.StringVar()
    category_dropdown = ttk.Combobox(add_window, textvariable=category_var, values=categories_names)
    category_dropdown.pack()
    category_dropdown.insert(0, product[5])
    category_dropdown.config(state="readonly")
    button_save = tk.Button(add_window, text="Enregistrer", bg="gray", fg="white", padx=5, pady=5, bd=0, activebackground="light gray", command=lambda: update_product(entry_name.get(), entry_description.get(),entry_price.get(), entry_quantity.get(), category_var.get(), product[0], add_window))
    button_save.pack(pady=20)

def update_product(name, description, price, quantity, category,id, add_window):
    pass
    for i in categories:
        if i[1] == category:
            id_category = i[0]

    crud_product.update(id,name, description, price, quantity, id_category)
    add_window.destroy() 
    get_data()


def add_product():
    global categories_names
    add_window = tk.Toplevel(root)
    add_window.geometry("400x400")
    add_window.title("Ajouter un produit")

    label_name = tk.Label(add_window, text="Nom")
    label_name.pack()
    entry_name = tk.Entry(add_window)
    entry_name.pack()

    label_description = tk.Label(add_window, text="Description")
    label_description.pack()
    entry_description = tk.Entry(add_window)
    entry_description.pack()

    label_price = tk.Label(add_window, text="Prix en €")
    label_price.pack()
    entry_price = tk.Entry(add_window)
    entry_price.pack()

    label_quantity = tk.Label(add_window, text="Quantité")
    label_quantity.pack()
    entry_quantity = tk.Entry(add_window)
    entry_quantity.pack()

    label_category = tk.Label(add_window, text="Catégorie")
    label_category.pack()
    category_var = tk.StringVar()
    category_dropdown = ttk.Combobox(add_window, textvariable=category_var, values=categories_names)
    category_dropdown.pack()
    category_dropdown.config(state="readonly")

    button_save = tk.Button(add_window, text="Enregistrer", bg="gray", fg="white", padx=5, pady=5, bd=0, activebackground="light gray", command=lambda: save_product(entry_name.get(), entry_description.get(),entry_price.get(), entry_quantity.get(), category_var.get(), add_window))
    button_save.pack(pady=20)

# Sauvegarde le produit
def save_product(name, description, price, quantity, category, add_window):
    pass
    for i in categories:
        if i[1] == category:
            id_category = i[0]

    crud_product.create(name, description, price, quantity, id_category)
    add_window.destroy() 
    get_data()


# # Création de l'interface graphique
# button = tk.Button(root, text='Afficher les produits', command=get_data)
# button.pack()
# button1.pack(side=tk.BOTTOM)

get_data()

# Lancement de l'interface graphique
root.mainloop()
connect.cursor.close()
connect.conn.close()