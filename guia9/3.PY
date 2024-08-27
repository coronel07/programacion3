import time
import matplotlib.pyplot as plt
from busqueda_lineal import busqueda_lineal
from busqueda_binaria import busqueda_binaria

# Listas de diferentes tamaños
listas = [list(range(100)), list(range(1000)), list(range(10000)), list(range(100000))]
elemento = 99999

# Almacenar tiempos
tiempos_lineal = []
tiempos_binaria = []

# Comparar tiempos
for lista in listas:
    # Búsqueda Lineal
    inicio_lineal = time.time()
    busqueda_lineal(lista, elemento)
    tiempo_lineal = time.time() - inicio_lineal
    tiempos_lineal.append(tiempo_lineal)
    
    # Búsqueda Binaria
    inicio_binaria = time.time()
    busqueda_binaria(lista, elemento)
    tiempo_binaria = time.time() - inicio_binaria
    tiempos_binaria.append(tiempo_binaria)
    
    print(f"Tamaño de la lista: {len(lista)}")
    print(f"Tiempo Búsqueda Lineal: {tiempo_lineal:.6f} segundos")
    print(f"Tiempo Búsqueda Binaria: {tiempo_binaria:.6f} segundos")
    print("-" * 50)

# Graficar los resultados
tamaños = [len(lista) for lista in listas]
plt.plot(tamaños, tiempos_lineal, label='Búsqueda Lineal')
plt.plot(tamaños, tiempos_binaria, label='Búsqueda Binaria')
plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.title('Comparación de Algoritmos de Búsqueda')
plt.legend()
plt.grid(True)
plt.show()
