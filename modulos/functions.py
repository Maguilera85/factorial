
# Función para calcular factorial
def factorial(n):
    for i in range(1, n):
        n *= i
    return n


def add_dict(user, number, factorial):
    dictionary = {}
    dictionary[user] = number, factorial
    return dictionary

if __name__ == "__main__":
    print(factorial(5))
    add = add_dict('miguel', 5, 120)
    print(add)