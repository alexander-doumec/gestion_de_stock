import tkinter as tk 
from tkinter import ttk


class Menu :
    def __init__(self, root, longueur, largeur, main_instance):
        self.root = root 
        self.main = main_instance
        self.root.title("Gestion des stocks")
        self.longueur = longueur
        self.largeur = largeur
        titre_label = ttk.Label(root, text="Gestion des stocks", font=("Times Nex Roman", 35))
        titre_label.pack(pady=25)
        options = ["Afficher les produits", "Ajouter un produit","Supprimer un produit", "Modifier un produit", "Quitter le programme"]

        for option in options :
            square_button = self.create_square_button(root, option, command=lambda o=option: self.main.choix_menu(o))
            square_button.pack(pady=10)

        # Centrer la fenêtre sur l'écran
        self.centrer_fenetre()

    def create_square_button(self, master, text, command):
        button = tk.Canvas(master, width=300, height=40, bg='orange')
        button.create_text(150, 20, text=text, font=("Times New Roman", 18), fill='white')
        button.bind('<Button-1>', lambda event: command())
        return button


    def centrer_fenetre(self):
        # Mettre à jour les tâches sans délai pour obtenir la taille correcte de la fenêtre
        self.root.update_idletasks()

        # Obtenir les dimensions de l'écran
        largeur_ecran = self.root.winfo_screenwidth()
        hauteur_ecran = self.root.winfo_screenheight()

        # Calculer les coordonnées pour centrer la fenêtre
        x_position = (largeur_ecran - self.longueur) // 2
        y_position = (hauteur_ecran - self.largeur) // 2

        # Définir la position de la fenêtre
        self.root.geometry(f"{self.longueur}x{self.largeur}+{x_position}+{y_position}")


if __name__ == "__main__":
    root = tk.Tk()
    root.mainloop()