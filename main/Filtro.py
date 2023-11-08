import cv2
import numpy as np

def filtrar(nombre):
    """
    Aplica un filtro a una imagen y devuelve una nueva imagen filtrada.

    Args:
        nombre (str): El nombre del archivo de imagen de entrada.

    Returns:
        numpy.ndarray: Una imagen filtrada representada como un arreglo numpy en formato RGBA.

    Ejemplo:
        >>> arreglo = filtrar("11838.jpg")
    """
    try:
        imagen = cv2.imread(nombre)
        if imagen is None:
            print(f"No se pudo abrir la imagen: {nombre}")
            return None

        ceros = np.array([80, 60, 60], dtype=np.uint8)
        limite = 0.95
        mask1 = np.all(imagen < ceros, axis=-1)
        epsilon = 1e-6
        rojo = imagen[..., 0] + epsilon
        mask2 = imagen[..., 2] / rojo < limite

        rgba_imagen = np.zeros((imagen.shape[0], imagen.shape[1], 4), dtype=np.uint8)
        rgba_imagen[..., :3] = imagen
        rgba_imagen[..., 3] = 255
        rgba_imagen[mask1, 3] = 0
        rgba_imagen[mask2, :3] = 0

        return rgba_imagen
    except Exception as e:
        print(f"Error al procesar la imagen: {str(e)}")
        return None

if __name__ == "__main__":
    arreglo = filtrar("11838.jpg")
    archivo_salida = "imagen_filtro.png"
    cv2.imwrite(archivo_salida, arreglo)
