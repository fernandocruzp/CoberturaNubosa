import cv2
import numpy as np

def filtrar(nombre):
    imagen=cv2.imread(nombre)
    arreglo=np.array(imagen)
    alto,ancho,prof=arreglo.shape
    rgba_imagen=np.zeros((arreglo.shape[0], arreglo.shape[1], 4), dtype=np.uint8)
    rgba_imagen[:, :, 0] = arreglo[:, :, 0]
    rgba_imagen[:, :, 1] = arreglo[:, :, 1]
    rgba_imagen[:, :, 2] = arreglo[:, :, 2]
    rgba_imagen[:, :, 3] = 255
    ceros=np.array([80,60,60])
    for i in range(alto):
        for j in range(ancho):
            if (arreglo[i,j]<ceros).all():
                rgba_imagen[i, j, 3] = 0
            elif float(arreglo[i,j][2]/arreglo[i,j][1]) < 0.95:
                rgba_imagen[i, j, :3] = 0
                rgba_imagen[i, j, 3] = 255
            else:
                rgba_imagen[i, j, :3] = 255
                rgba_imagen[i, j, 3] = 255
    return rgba_imagen



if __name__=="__main__":
    arreglo=filtrar("11838.jpg")
    archivo_salida = "imagen_filtro.png"
    cv2.imwrite(archivo_salida, arreglo)