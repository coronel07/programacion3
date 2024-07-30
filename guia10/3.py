import matplotlib.pyplot as plt
import numpy as np

def visualizar_puntos(imagen_path, resultados):
    imagen = Image.open(imagen_path).convert('L')
    img_array = np.array(imagen)
    
    plt.imshow(img_array, cmap='gray')
    x_coords, y_coords = zip(*resultados.keys())
    plt.scatter(x_coords, y_coords, color='red', s=1)
    plt.title('Puntos encontrados')
    plt.show()
