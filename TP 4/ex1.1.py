# Demande le nombre d'étudiants à l'utilisateur
nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
# déclaration d’une liste vide qui va contenir autant de notes que d'étudiants
notes = []



for i in range (nombreEtudiants):
    note = int(input("Rentrez vos notes : "))
    while note < 0 or note > 20:
        note = int(input(f"Entrez la note de l'étudiant {i + 1} (entre 0 et 20) : "))
        if note < 0 or note > 20:
            print("Erreur : La note doit être comprise entre 0 et 20.")
    notes.append(note)
    print("Votre note doit etre compris entre 0 et 0")
    notes.append(note)
    moyenne = sum(notes) / len(notes)
    print("Le moyenne de la classe est actuellement ",moyenne)