def busqueda_lineal(lista, elemento):
    for i, valor in enumerate(lista):
        if valor == elemento:
            return i
    return -1

