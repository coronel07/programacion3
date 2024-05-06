try:
    num_str = input("Ingrese un número: ")
    num = int(num_str)
    print("El número ingresado es:", num)
except ValueError:
    print("Error: Por favor ingrese un valor numérico válido.")
    