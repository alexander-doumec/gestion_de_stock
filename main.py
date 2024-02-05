import tkinter as tk
from utilisateur import Utilisateur
from menu import Menu
import sys
from tkinter import Label, Entry, Button, messagebox, scrolledtext

class Main(tk.Tk): # Héritage de tk.TK
    def __init__(self):
        super().__init__()
        self.manager = Utilisateur()
        self.menu()

    def menu(self):
        app = Menu(self, longueur=900, largeur=600, main_instance=self)  # Passage de self comme master
        self.mainloop()

#CRUD
    def createProduct(self):
        root = tk.Tk()
        root.title("Ajouter un produit")
        # Définir la géométrie pour agrandir la fenêtre
        root.geometry("700x500")  # Remplacez les dimensions par celles que vous préférez
        # Centrer la fenêtre par rapport à l'écran
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_position = (screen_width - 700) // 2
        y_position = (screen_height - 500) // 2
        root.geometry(f"700x500+{x_position}+{y_position}")
        # Configurer les colonnes pour qu'elles s'étirent horizontalement
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)

        # Configurer les lignes pour qu'elles s'étirent verticalement
        for i in range(6):
            root.rowconfigure(i, weight=1)
        # Création des labels et entry widgets pour chaque champ du produit
        Label(root, text="Nom du produit:").grid(row=0, column=0, sticky="e", pady=(7, 0))  # Aligner à droite, réduire le pady
        name_entry = Entry(root)
        name_entry.grid(row=0, column=1, sticky="w", pady=(7, 0), ipady=3)  # Aligner à gauche, réduire le pady et ipady

        Label(root, text="Description du produit:").grid(row=1, column=0, sticky="e", pady=(7, 0))  # Aligner à droite
        description_entry = Entry(root)
        description_entry.grid(row=1, column=1, sticky="w", pady=(7, 0), ipady=3)  # Aligner à gauche

        Label(root, text="Prix du produit:").grid(row=2, column=0, sticky="e", pady=(7, 0))  # Aligner à droite
        price_entry = Entry(root)
        price_entry.grid(row=2, column=1, sticky="w", pady=(7, 0), ipady=3)  # Aligner à gauche

        Label(root, text="Quantité de produit en stock:").grid(row=3, column=0, sticky="e", pady=(7, 0))  # Aligner à droite
        quantity_entry = Entry(root)
        quantity_entry.grid(row=3, column=1, sticky="w", pady=(7, 0), ipady=3)  # Aligner à gauche

        Label(root, text="ID de la catégorie:").grid(row=4, column=0, sticky="e", pady=(7, 0))  # Aligner à droite
        id_category_entry = Entry(root)
        id_category_entry.grid(row=4, column=1, sticky="w", pady=(7, 0), ipady=3)  # Aligner à gauche

        # Fonction pour récupérer les valeurs lorsque le bouton est cliqué
        def save_product():
            name = name_entry.get()
            description = description_entry.get()
            price = int(price_entry.get())
            quantity = int(quantity_entry.get())
            id_category = int(id_category_entry.get())

            # Appel de la méthode pour enregistrer le produit dans la base de données
            add_result = self.manager.createProduct(name, description, price, quantity, id_category)
            root.destroy()  # Fermer la fenêtre après avoir ajouté le produit

            if add_result:
                messagebox.showinfo("Succès", "Produit ajouté avec succès.")
            else:
                messagebox.showerror("Erreur", "Une erreur s'est produite lors de l'ajout du produit.")


        # Configurer la colonne 0 pour qu'elle s'étire et soit centrée
        root.columnconfigure(0, weight=1)
        # Bouton "Cancel"
        cancel_button = tk.Button(root, text="Annuler", command=root.destroy)
        cancel_button.grid(row=5, column=0, pady=10, sticky="nsew")  # Centrez dans la colonne 0
        # Bouton "Enregistrer le produit"
        save_button = tk.Button(root, text="Enregistrer", command=save_product)
        save_button.grid(row=5, column=1, pady=10, sticky="nsew")  # Centrez dans la colonne 1

        root.mainloop()



    # La Méthode READ
    def readProduit(self):
        # Créer une nouvelle fenêtre pour afficher les produits
        read_window = tk.Toplevel()
        read_window.title("Liste des Produits")
        # Ajouter une barre de défilement vertical
        scrollbar = tk.Scrollbar(read_window, orient=tk.VERTICAL)
        text_area = scrolledtext.ScrolledText(
            read_window, wrap=tk.WORD, width=80, height=50, yscrollcommand=scrollbar.set
        )
        scrollbar.config(command=text_area.yview)
        text_area.pack(padx=10, pady=10, side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        # Logique de read_produit sans utiliser insert
        text_content = ""
        text_content = "Liste complète des Produits :\n-----------------------------\n"
        for produit in self.manager.readproduit():
            text_content += f"id : {produit[0]}\n"
            text_content += f"Nom : {produit[1]}\n"
            text_content += f"Description : {produit[2]}\n"
            text_content += f"Prix : {produit[3]}\n"
            text_content += f"Quantité : {produit[4]}\n"
            text_content += f"id_catégorie : {produit[5]}\n"
            text_content += "----------------\n"

        text_area.configure(state='normal')  # Permet l'édition
        text_area.delete(1.0, tk.END)  # Efface le contenu actuel de la zone de texte
        text_area.insert(tk.END, text_content)  # Assigner le nouveau texte
        text_area.configure(state='disabled')  # Verrouiller le widget

        read_window.mainloop()
            
    # La Méthode UPDATE
    def modifierProduit(self):
        # Créer une nouvelle fenêtre pour modifier le produit
        modifier_window = tk.Tk()
        modifier_window.title("Modifier un Produit")

        # Définir la géométrie pour agrandir la fenêtre
        modifier_window.geometry("700x500")

        # Centrer la fenêtre par rapport à l'écran
        screen_width = modifier_window.winfo_screenwidth()
        screen_height = modifier_window.winfo_screenheight()
        x_position = (screen_width - 700) // 2
        y_position = (screen_height - 500) // 2

        modifier_window.geometry(f"700x500+{x_position}+{y_position}")

        # Configurer les colonnes pour qu'elles s'étirent horizontalement
        modifier_window.columnconfigure(0, weight=1)
        modifier_window.columnconfigure(1, weight=1)

        # Configurer les lignes pour qu'elles s'étirent verticalement
        for i in range(6):
            modifier_window.rowconfigure(i, weight=1)

        # Création des labels et entry widgets pour chaque champ du produit
        Label(modifier_window, text="ID du produit à modifier:").grid(row=0, column=0, sticky="e", pady=(7, 0))
        id_product_entry = Entry(modifier_window)
        id_product_entry.grid(row=0, column=1, sticky="w", pady=(7, 0), padx=(0, 5), ipady=3)  # Réduire l'espace horizontal

        Label(modifier_window, text="Nouveau nom du produit:").grid(row=1, column=0, sticky="e", pady=(7, 0))
        name_entry = Entry(modifier_window)
        name_entry.grid(row=1, column=1, sticky="w", pady=(7, 0), padx=(0, 5), ipady=3)  # Réduire l'espace horizontal

        Label(modifier_window, text="Nouvelle description du produit:").grid(row=2, column=0, sticky="e", pady=(7, 0))
        description_entry = Entry(modifier_window)
        description_entry.grid(row=2, column=1, sticky="w", pady=(7, 0), padx=(0, 5), ipady=3)  # Réduire l'espace horizontal

        Label(modifier_window, text="Nouveau prix du produit:").grid(row=3, column=0, sticky="e", pady=(7, 0))
        price_entry = Entry(modifier_window)
        price_entry.grid(row=3, column=1, sticky="w", pady=(7, 0), padx=(0, 5), ipady=3)  # Réduire l'espace horizontal

        Label(modifier_window, text="Nouvelle quantité de produit en stock:").grid(row=4, column=0, sticky="e", pady=(7, 0))
        quantity_entry = Entry(modifier_window)
        quantity_entry.grid(row=4, column=1, sticky="w", pady=(7, 0), padx=(0, 5), ipady=3)  # Réduire l'espace horizontal

        Label(modifier_window, text="Nouvel ID de la catégorie:").grid(row=5, column=0, sticky="e", pady=(7, 0))
        id_category_entry = Entry(modifier_window)
        id_category_entry.grid(row=5, column=1, sticky="w", pady=(7, 0), padx=(0, 5), ipady=3)  # Réduire l'espace horizontal

        # Fonction pour récupérer les valeurs lorsque le bouton est cliqué
        def sauvegarde_produit():
            try:
                id_product = int(id_product_entry.get())
                name = name_entry.get()
                description = description_entry.get()
                price = int(price_entry.get())
                quantity = int(quantity_entry.get())
                id_category = int(id_category_entry.get())
            except ValueError:
                messagebox.showerror("Erreur", "Veuillez entrer des valeurs numériques valides.")
                return

            # Appel de la méthode pour modifier le produit dans la base de données
            save_result = self.manager.modifierproduit(id_product, name, description, price, quantity, id_category)
            modifier_window.destroy()  # Fermer la fenêtre après avoir modifié le produit

            # Afficher une notification en fonction du résultat
            if save_result:
                messagebox.showinfo("Succès", "Produit modifié avec succès.")
            else:
                messagebox.showerror("Erreur", "Une erreur s'est produite lors de la modification du produit.")


        # Configurer la colonne 0 pour qu'elle s'étire et soit centrée
        modifier_window.columnconfigure(0, weight=1)

        # Bouton "Annuler"
        cancel_button = tk.Button(modifier_window, text="Annuler", command=modifier_window.destroy, width=15)
        cancel_button.grid(row=6, column=0, pady=10, sticky="nsew")

        # Bouton "Enregistrer la modification"
        save_button = tk.Button(modifier_window, text="Enregistrer", command=sauvegarde_produit, width=15)
        save_button.grid(row=6, column=1, pady=10, sticky="nsew")

        modifier_window.mainloop()

    # La Méthode DELETE
    def deleteProduct(self):
        delete_window = tk.Toplevel(self)
        delete_window.title("Supprimer un Produit")
        label = tk.Label(delete_window, text="Veuillez entrer l'ID du produit :")
        label.pack()
        entry = tk.Entry(delete_window)
        entry.pack()
        button = tk.Button(delete_window, text="Supprimer", command=lambda: self.gestion_suppression(entry.get(), delete_window))
        button.pack()

        # Obtenez la résolution de l'écran
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # Calculez la position pour centrer la fenêtre
        x_position = (screen_width - delete_window.winfo_reqwidth()) // 2
        y_position = (screen_height - delete_window.winfo_reqheight()) // 2
        # Définissez la géométrie pour centrer la fenêtre
        delete_window.geometry(f"+{x_position}+{y_position}")

    def gestion_suppression(self, id_produit, delete_window):
        try:
            id_produit = int(id_produit)
        except ValueError:
            messagebox.showerror("Erreur", "L'ID du produit est invalide. Veuillez entrer un nombre.")
            return
        try:
            deletion_result = self.manager.deleteproduit(id_produit)
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite lors de la suppression : {str(e)}")
            return
        if deletion_result:
            messagebox.showinfo("Succès", "Produit supprimé avec succès.")
        else:
            messagebox.showerror("Erreur", "Impossible de supprimer le produit. Veuillez vérifier l'ID.")


    # La Gestion des évènements
    def choix_menu(self, option):
        if option == "Afficher les produits":
            self.readProduit()
        elif option == "Ajouter un produit":
            self.createProduct()
        elif option == "Supprimer un produit":
            self.deleteProduct()
        elif option == "Modifier un produit":
            self.modifierProduit()
        elif option == "Quitter le programme":
            sys.exit()

if __name__ == "__main__":
    Main()