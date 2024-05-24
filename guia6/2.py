def leer_tabla_multiplicar():
  
    numero = int(input("Introduce un número entero entre 1 y 10: "))

    if numero < 1 or numero > 10:
        print("El número debe estar entre 1 y 10.")
        return 

    nombre_archivo = f"tabla-{numero}.txt"

    try:
       
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
           
            print(contenido)
    except FileNotFoundError:
       
        print(f"El archivo '{nombre_archivo}' no existe.")

leer_tabla_multiplicar()
