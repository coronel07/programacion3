class JugadorDeFutbol:
  def __init__(self, nombre, edad, posicion, equipo, pais, numero_camiseta, goles=0, asistencias=0, tarjetas_amarillas=0, tarjetas_rojas=0, premios=[]):
      self.nombre = nombre
      self.edad = edad
      self.posicion = posicion
      self.equipo = equipo
      self.pais = pais
      self.numero_camiseta = numero_camiseta
      self.goles = goles
      self.asistencias = asistencias
      self.tarjetas_amarillas = tarjetas_amarillas
      self.tarjetas_rojas = tarjetas_rojas
      self.premios = premios

  def actualizar_informacion(self, **kwargs):
      for key, value in kwargs.items():
          if hasattr(self, key):
              setattr(self, key, value)
      print("Información actualizada correctamente.")

  def calcular_promedio_goles(self):
      partidos_jugados = 10  # supongamos que jugó 10 partidos
      promedio_goles = self.goles / partidos_jugados
      return promedio_goles

  def es_goleador(self):
      return self.goles > 10  # supongamos que un goleador es quien ha marcado más de 10 goles

  def agregar_premio(self, premio):
      self.premios.append(premio)
      print(f"Premio '{premio}' agregado correctamente.")

  def eliminar_premio(self, premio):
      if premio in self.premios:
          self.premios.remove(premio)
          print(f"Premio '{premio}' eliminado correctamente.")
      else:
          print("El premio especificado no está en la lista.")

  def actualizacion_estadisticas(self):
      print("Estadísticas actualizadas.")

def mostrar_menu():
  print("\nMenú:")
  print("1. Crear nuevo jugador de fútbol")
  print("2. Mostrar información de un jugador existente")
  print("3. Actualizar información de un jugador existente")
  print("4. Calcular promedio de goles por partido de un jugador")
  print("5. Verificar si un jugador es un goleador")
  print("6. Agregar premio o reconocimiento a un jugador")
  print("7. Eliminar premio o reconocimiento de un jugador")
  print("8. Salir")

def main():
  jugadores = []

  while True:
      mostrar_menu()
      opcion = input("Seleccione una opción: ")

      if opcion == "1":
          nombre = input("Ingrese el nombre del jugador: ")
          edad = int(input("Ingrese la edad del jugador: "))
          posicion = input("Ingrese la posición del jugador: ")
          equipo = input("Ingrese el equipo actual del jugador: ")
          pais = input("Ingrese el país de origen del jugador: ")
          numero_camiseta = int(input("Ingrese el número de camiseta del jugador: "))
          nuevo_jugador = JugadorDeFutbol(nombre, edad, posicion, equipo, pais, numero_camiseta)
          jugadores.append(nuevo_jugador)
          print("Jugador creado correctamente.")

      elif opcion == "2":
          if jugadores:
              nombre = input("Ingrese el nombre del jugador: ")
              for jugador in jugadores:
                  if jugador.nombre == nombre:
                      print("Información del jugador:")
                      print(vars(jugador))
                      break
              else:
                  print("No se encontró ningún jugador con ese nombre.")
          else:
              print("No hay jugadores registrados.")

      elif opcion == "3":
          if jugadores:
              nombre = input("Ingrese el nombre del jugador: ")
              for jugador in jugadores:
                  if jugador.nombre == nombre:
                      atributo = input("Ingrese el nombre del atributo a actualizar: ")
                      valor = input(f"Ingrese el nuevo valor para {atributo}: ")
                      jugador.actualizar_informacion(**{atributo: valor})
                      break
              else:
                  print("No se encontró ningún jugador con ese nombre.")
          else:
              print("No hay jugadores registrados.")

      elif opcion == "4":
          if jugadores:
              nombre = input("Ingrese el nombre del jugador: ")
              for jugador in jugadores:
                  if jugador.nombre == nombre:
                      promedio_goles = jugador.calcular_promedio_goles()
                      print(f"El promedio de goles por partido de {nombre} es: {promedio_goles}")
                      break
              else:
                  print("No se encontró ningún jugador con ese nombre.")
          else:
              print("No hay jugadores registrados.")

      elif opcion == "5":
          if jugadores:
              nombre = input("Ingrese el nombre del jugador: ")
              for jugador in jugadores:
                  if jugador.nombre == nombre:
                      if jugador.es_goleador():
                          print(f"{nombre} es un goleador.")
                      else:
                          print(f"{nombre} no es un goleador.")
                      break
              else:
                  print("No se encontró ningún jugador con ese nombre.")
          else:
              print("No hay jugadores registrados.")

      elif opcion == "6":
          if jugadores:
              nombre = input("Ingrese el nombre del jugador: ")
              for jugador in jugadores:
                  if jugador.nombre == nombre:
                      premio = input("Ingrese el premio o reconocimiento a agregar: ")
                      jugador.agregar_premio(premio)
                      break
              else:
                  print("No se encontró ningún jugador con ese nombre.")
          else:
              print("No hay jugadores registrados.")

      elif opcion == "7":
          if jugadores:
              nombre = input("Ingrese el nombre del jugador: ")
              for jugador in jugadores:
                  if jugador.nombre == nombre:
                      premio = input("Ingrese el premio o reconocimiento a eliminar: ")
                      jugador.eliminar_premio(premio)
                      break
              else:
                  print("No se encontró ningún jugador con ese nombre.")
          else:
              print("No hay jugadores registrados.")

      elif opcion == "8":
          print("¡Hasta luego!")
          break

      else:
          print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
  main()
