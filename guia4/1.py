class JugadorDeFutbol:
    def __init__(self, nombre, edad, posicion, equipo, pais, numero_camiseta):
        self.nombre = nombre
        self.edad = edad
        self.posicion = posicion
        self.equipo = equipo
        self.pais = pais
        self.numero_camiseta = numero_camiseta
        self.goles_marcados = 0
        self.asistencias = 0
        self.tarjetas_amarillas = 0
        self.tarjetas_rojas = 0
        self.premios = []

    def actualizar_estadisticas(self, goles, asistencias, amarillas, rojas):
        self.goles_marcados += goles
        self.asistencias += asistencias
        self.tarjetas_amarillas += amarillas
        self.tarjetas_rojas += rojas
        print("Estadísticas")

    def calcular_promedio_goles(self):
        partidos_jugados = 10  
        return self.goles_marcados / partidos_jugados

    def es_goleador(self):
        return self.goles_marcados > 10 

    def agregar_premio(self, premio):
        self.premios.append(premio)
        print("Premio")

    def eliminar_premio(self, premio):
        if premio in self.premios:
            self.premios.remove(premio)
            print("Premio eliminado")
        else:
            print("El premio no esta")

def menu_interactivo():
    print("Bienvenido al menú interactivo del jugador")
    print("1) Crear un nuevo jugador")
    print("2) Mostrar la información de algun jugador")
    print("3) Actualizar la información de algun jugador ")
    print("4) Calcular el promedio de goles de un jugador en un partido")
    print("5) Ver si un jugador es un goleador.")
    print("6) Agregar un premio a un jugador.")
    print("7) Eliminar un premio de un jugador.")
    print("8) Salir")

    opcion = input("número de la opción que desea")

    if opcion == "1":
        nombre = input("poner el nombre del jugador: ")
        edad = int(input("poner la edad del jugador: "))
        posicion = input("poner la posición del jugador: ")
        equipo = input("poner el equipo actual del jugador: ")
        pais = input("poner el país del jugador: ")
        numero_camiseta = int(input("poner la dorsal del jugador: "))
        nuevo_jugador = JugadorDeFutbol(nombre, edad, posicion, equipo, pais, numero_camiseta)
        print("Jugador creado correctamente.")

menu_interactivo()
