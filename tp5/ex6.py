# avoir une chaine et verifier le nom figure dans le chaine de ch. len renvie le longeur de chaine de ch mais .
# on utilise boucle for sans utilisier len. for i in s : ...

chain=input("")
count=0
chain=chain.lower()
for i in range(len(chain)):
    if chain[i]== 'a' or chain [i]