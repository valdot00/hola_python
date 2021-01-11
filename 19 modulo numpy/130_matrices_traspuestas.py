# arrays o matrices traspuestas (cambiar ordenadamente las filas por las columnas)

import numpy as np

#para crear 3 filas y 5 columnas np.arange(15).reshape((filas,columnas))
arrray = np.arange(15).reshape((3,5))

print(arrray[1][1])

print(arrray)

#para cambiar las filas por las columnas

array_tras = array.T 

print(array_tras)
