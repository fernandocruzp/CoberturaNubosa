import numpy as np
import cv2
import sys
import Filtro

def indiceDeCobertura(arreglo):
    """
    Busca un ticket en un archivo CSV y devuelve el clima de la ciudad de origen y destino asociada al ticket.   

    Args: 
    arreglo: con 3 dimensiones, ancho, alto y rgb 

    Returns:
        float: cobertura nubosa
    """
    alfa=arreglo[...,3]
    total=np.sum(alfa>0)
    nubes=np.sum(np.all(arreglo[:,:,:4]==[255,255,255,255],axis=2))
    print(total,nubes)
    return float(nubes/total)