argument = int(input("Rentrez votre argument"))

La_table_de_multiplication = []

for i in range(1, 11):
    result = argument * i
    La_table_de_multiplication.append(result)

    print(La_table_de_multiplication)