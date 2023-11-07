import numpy as np
import cv2
import sys
import Filtro

def indiceDeCobertura(arreglo):
    alto,ancho,prof=arreglo.shape
    total,nubes=0,0
    arr_nubes=np.array([255,255,255,255])
    cielo=np.array([0,0,0,255])
    for i in range(alto):
        for j in range(ancho):
            if arreglo[i,j][3]==0:
                pass
            if np.array_equal(arreglo[i,j], arr_nubes):
                nubes+=1
            total+=1
    return float(nubes/total)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python programa.py archivo_entrada.jpg [S]")
        sys.exit(1)

    archivo_entrada = sys.argv[1]
    arreglo=Filtro.filtrar(archivo_entrada)
    indice=indiceDeCobertura(arreglo)
    print("CCI: ", indice)
    if len(sys.argv) == 3 and sys.argv[2].lower() == "s":
        archivo_salida = f"{archivo_entrada}-seg.png"
        cv2.imwrite(archivo_salida, arreglo)
