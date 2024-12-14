nombre = float(input("Vous cherchez la table de multiplication de quel nombre ? "))


multilist = []

for i in range(10):
    multilist = nombre * i
    multilist.append(round(multilist, 1))


for i, multilist in enumerate(multilist):
    print(f"{nombre} * {i} = {multilist}")