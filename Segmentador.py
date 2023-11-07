import numpy as np
import cv2
import sys
import Filtro

def indiceDeCobertura(arreglo):
    alfa=arreglo[...,3]
    total=np.sum(alfa>0)
    nubes=np.sum(np.all(arreglo[:,:,:4]==[255,255,255,255],axis=2))
    print(total,nubes)
    return float(nubes/total)