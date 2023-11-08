import unittest
import os
import subprocess
import cv2
import numpy as np
from main import Filtro
from main import Segmentador

class TestProgramas(unittest.TestCase):
    def test_filtrar_correctamente(self):
        arreglo = Filtro.filtrar("11838.jpg")
        self.assertIsNotNone(arreglo)
        self.assertIsInstance(arreglo, np.ndarray)
        self.assertEqual(arreglo.shape[-1], 4)  # Asegurarse de que la imagen sea RGBA

    def test_filtrar_con_nombre_incorrecto(self):
        arreglo = Filtro.filtrar("imagen_que_no_existe.jpg")
        self.assertIsNone(arreglo)

   
    def test_indice_de_cobertura(self):
        imagen = np.zeros((100, 100, 4), dtype=np.uint8)
        imagen[..., 3] = 255  # Imagen completamente opaca
        indice = Segmentador.indiceDeCobertura(imagen)
        self.assertEqual(indice, 0.0)

if __name__ == "__main__":
    unittest.main()
