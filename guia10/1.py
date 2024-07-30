from PIL import Image

def busqueda_en_imagen(imagen_path, tono):
   
    imagen = Image.open(imagen_path).convert('L')
    ancho, alto = imagen.size
    resultados = {}

    for y in range(alto):
        for x in range(ancho):
            gris = imagen.getpixel((x, y))
            if gris == tono:
                resultados[(x, y)] = gris

    return resultados
