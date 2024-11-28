import random

a = random.randint(1, 100)
compteur = 0

while True:
    v = int(input("Rentrez un nombre : "))
    compteur += 1
    print("C'est votre",compteur, "tentative")
    if v == a:
        print("Vous avez trouvez le nombre mystere qui était : ",a)
        break
    if v > a:s
        print("Votre nombre est trop grand")
    else:
        print("Votre nombre est trop petit")
