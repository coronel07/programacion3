try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 / num2
    print("El resultado de la división es:", resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
