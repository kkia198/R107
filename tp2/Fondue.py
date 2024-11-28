base = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400


convives = int(input("Nombre de convives"))

print("La recette de la fondue pour 4 perssonnes est composé de fromage", fromage,"et d'eau",eau,"d'ail",ail,"pain",pain)


fromage = fromage * convives / base
print("Il faut donc fromage", fromage)
eau = eau * convives / base
print("Il faut donc eau", eau)
ail = ail * convives / base
print("Il faut donc ails", ail)
pain = pain * convives / base
print("Il faut donc ails", pain)
