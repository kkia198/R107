s=input("entrez unphrase")
temp=""
for i in range(len(s)):
    if s[i].isalpha():
        temp+=s[i]

      #on convertit en minuscule pour éviter problèmes de cast :
      test = temp.lower()

    leftpos=0
    rightpos=len(test) - 1
    palindrom=true
    while ((leftpos<rightpos) and palindrom)

        palindrom   continue....


 if palindrom:
     print("c'est un palindrome")
 else:
     print("non , ce n'est pas un palindrome")