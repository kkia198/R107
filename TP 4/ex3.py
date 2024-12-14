def get_vector_components(prompt, n):
    """Get the components of a vector from the user."""
    vector = []
    for i in range(n):
        while True:
            try:
                component = int(input(f"{prompt}[{i}] = "))
                vector.append(component)
                break
            except ValueError:
                print("Veuillez entrer un entier.")
    return vector

def calculate_dot_product(v1, v2):
    """Calculate the dot product of two vectors."""
    if len(v1) != len(v2):
        raise ValueError("Les vecteurs doivent avoir la même taille.")
    return sum(a * b for a, b in zip(v1, v2))

def main():
    nMax = 10
    while True:
        try:
            n = int(input(f"Quelle est la taille de vos vecteurs [entre 1 et {nMax}] ? "))
            if 1 <= n <= nMax:
                break
            else:
                print(f"Veuillez entrer une valeur comprise entre 1 et {nMax}.")
        except ValueError:
            print("Veuillez entrer un entier.")

    print("Saisie du premier vecteur :")
    v1 = get_vector_components("v1", n)

    print("Saisie du second vecteur :")
    v2 = get_vector_components("v2", n)

    dot_product = calculate_dot_product(v1, v2)
    print(f"Le produit scalaire de v1 par v2 vaut {dot_product}")

if __name__ == "__main__":
    main()
