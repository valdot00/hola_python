# INDEXACION CON ARRAYS

import numpy as np

array = np.arange(0,11)

print(array)

array([0:3]) #crea un array del 0 al 3 menos 1   

print(array)

array([:])#muestra el array original

array_copia = array.copy()

array_copia[0:3] = 20

array2 = np.array([1,2,3],[4,5,6],[7,8,9])

print(array2)

array2[0]

print(array2[0]) #imprime toda la pocision 0

print(array2[1][0]) #imprime la segunda fila primer numero






