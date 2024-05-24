def mostrar_linea_tabla_multiplicar():
    try:
        n = int(input("Introduce un número entero entre 1 y 10 para n: "))
        m = int(input("Introduce un número entero entre 1 y 10 para m: "))
        
        if n < 1 or n > 10 or m < 1 or m > 10:
            print("Ambos números deben estar entre 1 y 10.")
            return  

        nombre_archivo = f"tabla-{n}.txt"

        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            if m <= len(lineas):
                print(lineas[m-1].strip())
            else:
                print(f"El archivo '{nombre_archivo}' no tiene tantas líneas.")
    
    except ValueError:
        print("Por favor, introduce números enteros válidos.")
    except FileNotFoundError:
        print(f"El archivo 'tabla-{n}.txt' no existe.")

mostrar_linea_tabla_multiplicar()
