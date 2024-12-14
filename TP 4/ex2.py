nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
somme = 0.0

notes = []
for i in range(nombreEtudiants):
    while True:
        note = float(input(f"Note etudiant {i} : "))
        if 0 <= note <= 20:
            notes.append(note)
            somme += note
            break
        else:
            print("La note doit être comprise entre 0 et 20. Veuillez réessayer.")


moyenne = somme / nombreEtudiants

print(f"\nMoyenne de classe : {moyenne:.2f}\n")

print("Numéro de l'Etudiant | note | ecart a la moyenne")
for i, note in enumerate(notes):
    ecart = note - moyenne
    print(f"{i} | {note:.1f} | {ecart:.2f}")