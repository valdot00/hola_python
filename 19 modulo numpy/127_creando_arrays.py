#creando arrays

import numpy as np

np.zeros(4)

print(np.zeros(4))

np.ones(4)

print(np.ones(4))

np.arange(5)

print(np.arange(5))

np.arange(10)

print(np.arange(10))

np.arange(2,20,3)

print(np.arange(2,20,3))

lista = [1,2,3,4]
arrayl=np.array(lista)

print(lista)

lista = [1,2,3,4]
lista2 = [5,6,7,8]
lista_doble = (lista,lista2)

print(lista_doble)

array_doble = np.array(lista_doble)

print(array_doble)

print(array_doble.shape)

print(array_doble.dtype)
