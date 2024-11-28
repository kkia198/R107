n = int(input("Entrez un nombre : "))
factorielle = 1

for i in range(1,n + 1):
    factorielle *= i

print(f"La factorielle de {n} est {factorielle}")
