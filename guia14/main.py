# main.py
from temporizador import medir_tiempo

# Importa los algoritmos de ordenamiento
from algoritmo_burbuja import ordenamiento_burbuja
from algoritmo_seleccion import ordenamiento_seleccion
from algoritmo_insercion import ordenamiento_insercion
from algoritmo_rapido import ordenamiento_rapido
from algoritmo_fusion import ordenamiento_fusion

# Lista de ejemplo
listas = [
    [5, 2, 9, 1, 5, 6],
    [3.2, 2.4, 5.1, 1.9],
    ['z', 'a', 'b', 'x']
]

# Probar cada algoritmo
for lista in listas:
    print(f"Original: {lista}")
    print(f"Burbuja: {ordenamiento_burbuja(lista[:])}")
    print(f"Selección: {ordenamiento_seleccion(lista[:])}")
    print(f"Inserción: {ordenamiento_insercion(lista[:])}")
    print(f"Rápido: {ordenamiento_rapido(lista[:])}")
    print(f"Fusión: {ordenamiento_fusion(lista[:])}")
    print()
    
# Medir tiempos de ejecución
for lista in listas:
    print(f"Tiempos para la lista: {lista}")
    print(f"Burbuja: {medir_tiempo(ordenamiento_burbuja, lista[:])} segundos")
    print(f"Selección: {medir_tiempo(ordenamiento_seleccion, lista[:])} segundos")
    print(f"Inserción: {medir_tiempo(ordenamiento_insercion, lista[:])} segundos")
    print(f"Rápido: {medir_tiempo(ordenamiento_rapido, lista[:])} segundos")
    print(f"Fusión: {medir_tiempo(ordenamiento_fusion, lista[:])} segundos")
    print()
