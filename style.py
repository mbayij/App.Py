import tkinter as tk
from tkinter import messagebox

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Gestion de Notes Étudiantes")
fenetre.geometry("500x600")

# Dictionnaire pour stocker les étudiants
etudiants = {}

# ---------- FONCTIONS ----------

def ajouter_etudiant():
    matricule = entry_matricule.get().strip()
    nom = entry_nom.get().strip()

    if matricule == "" or nom == "":
        messagebox.showwarning("Champs manquants", "Veuillez remplir tous les champs.")
        return

    if matricule in etudiants:
        messagebox.showwarning("Doublon", f"L'étudiant {matricule} existe déjà.")
        return

    etudiants[matricule] = {"nom": nom, "notes": {}}
    liste_etudiants.insert(tk.END, f"{matricule} - {nom}")
    messagebox.showinfo("Ajouté", f"L'étudiant {nom} a été ajouté.")
    entry_matricule.delete(0, tk.END)
    entry_nom.delete(0, tk.END)

def ajouter_note():
    selection = liste_etudiants.curselection()
    if not selection:
        messagebox.showwarning("Sélection requise", "Veuillez sélectionner un étudiant.")
        return

    ligne = liste_etudiants.get(selection[0])
    matricule = ligne.split(" - ")[0]
    matiere = entry_matiere.get().strip()
    note_str = entry_note.get().strip()

    if matiere == "" or note_str == "":
        messagebox.showwarning("Champs manquants", "Veuillez entrer une matière et une note.")
        return

    try:
        note = float(note_str)
    except ValueError:
        messagebox.showerror("Erreur", "La note doit être un nombre.")
        return

    etudiants[matricule]["notes"][matiere] = note
    messagebox.showinfo("Note ajoutée", f"{matiere} : {note} ajoutée à {etudiants[matricule]['nom']}.")
    entry_matiere.delete(0, tk.END)
    entry_note.delete(0, tk.END)

def afficher_releve():
    selection = liste_etudiants.curselection()
    if not selection:
        messagebox.showwarning("Sélection requise", "Veuillez sélectionner un étudiant.")
        return

    ligne = liste_etudiants.get(selection[0])
    matricule = ligne.split(" - ")[0]
    etu = etudiants[matricule]

    notes = etu["notes"]
    if not notes:
        messagebox.showinfo("Relevé", f"{etu['nom']} n’a pas encore de notes.")
        return

    texte = f"Relevé de : {etu['nom']} ({matricule})\n"
    texte += "--------------------------\n"
    total = 0
    for matiere, note in notes.items():
        texte += f"{matiere} : {note}\n"
        total += note
    moyenne = total / len(notes)
    resultat = "Admis" if moyenne >= 10 else "Ajourné"
    texte += f"\nMoyenne : {moyenne:.2f}\nRésultat : {resultat}"

    messagebox.showinfo("Relevé de notes", texte)

# ---------- INTERFACE ----------

# Section ajout étudiant
tk.Label(fenetre, text="Matricule :").pack()
entry_matricule = tk.Entry(fenetre)
entry_matricule.pack()

tk.Label(fenetre, text="Nom :").pack()
entry_nom = tk.Entry(fenetre)
entry_nom.pack()

tk.Button(fenetre, text="Ajouter Étudiant", command=ajouter_etudiant).pack(pady=5)

# Liste des étudiants
tk.Label(fenetre, text="Étudiants enregistrés :").pack()
liste_etudiants = tk.Listbox(fenetre)
liste_etudiants.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

# Section ajout matière et note
tk.Label(fenetre, text="Matière :").pack()
entry_matiere = tk.Entry(fenetre)
entry_matiere.pack()

tk.Label(fenetre, text="Note :").pack()
entry_note = tk.Entry(fenetre)
entry_note.pack()

tk.Button(fenetre, text="Ajouter Note", command=ajouter_note).pack(pady=5)

# Bouton affichage relevé
tk.Button(fenetre, text="Afficher Relevé", command=afficher_releve).pack(pady=10)

# Lancer l'application
fenetre.mainloop()
