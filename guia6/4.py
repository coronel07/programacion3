archivo_texto = "listin.txt"

def nuevoUsuario():
    nombre = input("Ingrese su nombre:")
    telefono = int(input("Ingrese su número:"))
    try:
        with open(archivo_texto, "a") as archivo:
            archivo.write(f"{nombre}, {telefono}\n")

    except FileNotFoundError:   
        print(f"El archivo '{archivo_texto}' no fue encontrado.")
        with open(archivo_texto, "w") as archivo:
            archivo.writelines(f"{nombre}, {telefono}\n")

    except IOError:
        print(f"No se pudo abrir el archivo '{archivo_texto}'.")


def borrarNum():
    nombre = input("Ingrese el nombre de usuario que desea borrar el número:")
    try:
        with open(archivo_texto, "r") as archivo:
            lineas = archivo.readlines()
        
        with open(archivo_texto, "w") as archivo:
            for linea in lineas:
                if nombre not in linea:
                    archivo.write(f"{linea} \n")
                elif nombre in linea:
                    archivo.write(f"{nombre} \n")

    except IOError:
        print(f"No se pudo abrir el archivo '{archivo_texto}'.")


def leerArchivo():
    try:
        with open(archivo_texto, "r") as archivo:
            tablas = archivo.read()
            print(tablas)

    except FileNotFoundError:
        print(f"El archivo '{archivo_texto}' no fue encontrado.")

    except IOError:
        print(f"No se pudo abrir el archivo '{archivo_texto}'.")


def mostrar_menu():
    while True:
        menu_inicial()
        opcion = input("Seleccione el número opción deseado:")

        if opcion == "1":
            nuevoUsuario()

        elif opcion == "2":
            borrarNum()

        elif opcion == "3":
            leerArchivo()

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")


def menu_inicial():
    print("Bienvenido, elige una de las opciones:")
    print("1 - Crear usuario")
    print("2 - Borrar teléfono")
    print("3 - Leer archivo")
    print("4 - Salir")

mostrar_menu()