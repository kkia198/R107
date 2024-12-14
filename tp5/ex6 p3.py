ch=input("merci de donner la caine ").lower()
m="wagon"
occu=-1

l=len(m)
for i in range(len(ch)-l+1):

    if ch[i:l+i]==m:
        occu=1
        print("f la chaine {m} est bien une sous chaine de {ch}")