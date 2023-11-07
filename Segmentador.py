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