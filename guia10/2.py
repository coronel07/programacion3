from PIL import Image
import time

def busqueda_en_imagen(imagen_path, tono):
    pass
def prueba_busqueda(imagen_path, tono):
    inicio = time.time()
    resultados = busqueda_en_imagen(imagen_path, tono)
    fin = time.time()
    tiempo_ejecucion = fin - inicio
    print(f"Tiempo de ejecución: {tiempo_ejecucion:.4f} segundos")
    return resultados

if __name__ == "__main__":
    resultados = prueba_busqueda('imagen_gris.png', 128)
    print(f"Píxeles encontrados: {len(resultados)}")
