import tkinter as tk
from tkinter import messagebox

# Créer la fenêtre principale 
fenetre = tk.Tk()
fenetre.title("Gestion des Étudiants")
fenetre.geometry("400x300")

# Dictionnaire pour stocker les étudiants
etudiants = {}

# Fonction pour ajouter un étudiant
def ajouter_etudiant():
    # Récupérer les données saisies
    matricule = entry_matricule.get().strip()
    nom = entry_nom.get().strip()

    # Vérifier si les champs sont vides
    if matricule == "" or nom == "":
        messagebox.showwarning("Champs manquants", "Veuillez remplir tous les champs.")
        return

    # Vérifier si le matricule existe déjà
    if matricule in etudiants:
        messagebox.showwarning("Doublon", f"L'étudiant avec le matricule {matricule} existe déjà.") 
        return

    # Ajouter l'étudiant au dictionnaire
    etudiants[matricule] = {"nom": nom, "notes": []}

    # Afficher l'étudiant dans la liste visible
    liste_etudiants.insert(tk.END, f"{matricule} - {nom}")    
    # Afficher un message de confirmation
    messagebox.showinfo("Ajout réussi", f"L'étudiant {nom} a été ajouté avec succès.")

    # Vider les champs après l'ajout
    entry_matricule.delete(0, tk.END)
    entry_nom.delete(0, tk.END)

# Interface : champs matricule et nom
label_matricule = tk.Label(fenetre, text="Matricule :")
label_matricule.pack()
entry_matricule = tk.Entry(fenetre)
entry_matricule.pack()

label_nom = tk.Label(fenetre, text="Nom :")
label_nom.pack()
entry_nom = tk.Entry(fenetre)
entry_nom.pack()

# Bouton Ajouter
btn_ajouter = tk.Button(fenetre, text="Ajouter", command=ajouter_etudiant)
btn_ajouter.pack(pady=10)

# Liste pour afficher les étudiants
liste_etudiants = tk.Listbox(fenetre)
liste_etudiants.pack(fill=tk.BOTH, expand=True)


# Lancer la fenêtre
fenetre.mainloop()

 


