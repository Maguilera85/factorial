
# Función para calcular factorial
def factorial(n):
    for i in range(1, n):
        n *= i
    return n



if __name__ == "__main__":
    print(factorial(5))