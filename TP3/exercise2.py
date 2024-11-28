import time


entier = int(input("Rentrez un nombre positif : "))

for i in range(entier):
    entier -= 1
    time.sleep(1)
    print(entier)
tp3 lecture de 10 valeur
i = 0
while i < 10:
    nbr = float(input("Entrez un nombre réel : "))
    while nbr >= 20:
        nbr = float(input("Sasisez un nombre inférieur a 20 : "))
    print(f"Nombre saisi : ", nbr)
    if nbr < 10:
        print("Votre nombre est strictement inférieur à 10")
    elif nbr >= 10 and nbr < 15:
        print("Votre nombre est supérieur ou égal à 10 mais inférieur à 15")
    else:
        print("Votre nombre est supérieur ou égal à 15")
    i += 1

