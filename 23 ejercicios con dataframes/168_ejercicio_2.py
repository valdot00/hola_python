# ejercicio

#crear 2 array con 9 numeros aleatorios enteros entre los valores 0 y 100
#cambiar el formato de los arrays en una estructura de 3 filas por 3 columnas
#crear 2 dataframe con esos arrays
#concatenar esos 2 dataframes

import pandas as pd

from pandas.core.indexes.base import Index

import numpy as np

array1 = np.random.randint(0,100,9)

array1 = array1.reshape(3,3)

print(array1)

array2 = np.random.randint(0,100,9).reshape(3,3)

print(array2)

dataframe1 = pd.DataFrame(array1)

dataframe2 = pd.DataFrame(array2)

print(dataframe1)

print(dataframe2)

dataframe_concatenacion = pd.concat([dataframe2,dataframe1],ignore_index=True)

print(dataframe_concatenacion)