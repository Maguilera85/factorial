import modulos as mod 


while True:
    name = input("¿Cuál es tu nombre?\n >> ")
    number = int(input("Ingrese un número entero, para calcular su factorial\n >> "))
    result = mod.factorial(number)
    print(name + ", el resultado es: " + str(result))
    exit = str(input("¿Desea seguir usando la app? C/ontinuar o S/alir\n >> "))
    if exit == "C" or exit == "c" or exit == "continuar":
        continue
    elif exit == "S" or exit == "s" or exit == "salir":
        print("¡Hasta pronto!")
        break