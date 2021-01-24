# ejercicio 2

#1.- crear una lista con numeros del 10 al 19
#2.- crear otra lista con numeros del 50 al 59
#3.- crear una matriz 2x10 con las lista anteriores
#4.- crearotra matriz que cuyos valores sean iguales a la matriz
# anterior multiplicada por 2

import numpy as np

lista1 = np.arange(10,20)

print(lista1)

lista2 = np.arange(50,60)

listadoble = (lista1,lista2)

matriz = np.array(listadoble)

print(listadoble)

print(matriz.shape)

matriz_multi = matriz * 2

print(matriz_multi)

