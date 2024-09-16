import time

def medir_tiempo(func, lista):
    inicio = time.time()
    func(lista)
    fin = time.time()
    return fin - inicio
