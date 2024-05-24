def guardar_tabla_multiplicar():
    numero = int(input("Introduce un número entero entre 1 y 10: "))

    if numero < 1 or numero > 10:
        print("El número debe estar entre 1 y 10.")
        return 

    nombre_archivo = f"tabla-{numero}.txt"

    with open(nombre_archivo, 'w') as archivo:
        for i in range(1, 11):
            linea = f"{numero} x {i} = {numero * i}\n"
            archivo.write(linea)

    print(f"Tabla de multiplicar del {numero} guardada en '{nombre_archivo}'.")

guardar_tabla_multiplicar()
