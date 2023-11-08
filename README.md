# CoberturaNubosa
Programa que dada una fotografía de la bóveda celeste se calcula el índice de cobertura nubosa, es decir la proporción de la bóveda celeste cubierta por nubes.

## Colaboradores
* Cruz Pineda Fernando
* Espinosa Roque Rebeca
* Flores Carrillo Itzel Paola
* Marquéz Corona Danna Lizette

## Instalación 
```
$ git clone [liga del repositorio]
$ cd ../CoberturaNubosa
$ pip install numpy
$ pip install opencv-python
```
Se asume que se usa el instalador de paquetes *pip* de Pyhton, métodos alternativos también son aceptables.

## Uso 
Para correr el programa se debe posicionar en el directorio ```../CoberturaNubosa/main``` y utilizar el comando:
```
$ python Segmentador.py [nombreImagen]
```
O bien si se requiere también la imagen procesada:
```
$ python Segmentador.py [nombreImagen] s
```
**Nota** La imagen a procesar debe de estar en el directorio ```../CoberturaNubosa/main```

## Tecnologías utilizadas
* **NumPy** - NumPy es una biblioteca fundamental para el manejo de matrices y arreglos multidimensionales en Python. Su eficiencia y facilidad de uso serán cruciales para realizar operaciones de procesamiento de imágenes.
* **OpenCV** - OpenCV es una biblioteca de visión por computadora de código abierto que proporciona una amplia gama de funciones y algoritmos para el procesamiento de imágenes. Será fundamental para tareas como la
detección de bordes, la eliminación de ruido y la segmentación de objetos en las imágenes. 
