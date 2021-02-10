# operaciones 

import pandas as pd
from typing_extensions import runtime
import numpy as np

serie1 = pd.Series([0,1,2],index=['a','b','c',])

print(serie1)

serie2 = pd.Series([3,4,5,6],index=['a','b','c','d'])

print(serie2)

print(serie1+serie2)

lista_valores = np.arange(4).reshape(2,2)

print(lista_valores)

lista_indices = list('ab')

print(lista_indices)

lista_columnas = list('12')

print(lista_columnas)

dataframe = pd.DataFrame(lista_valores,index=lista_indices,columns=lista_columnas)

print(dataframe)

lista_valores_2 = np.arange(9).reshape(3,3)

print(lista_valores_2)

lista_indices_2 = list('abc')

print(lista_indices_2)

lista_columnas_2 = list('123')

print(lista_columnas_2)

dataframe2 = pd.DataFrame(lista_valores_2,index=lista_indices_2,columns=lista_columnas_2)

print(dataframe2)

print(dataframe+dataframe2)

dataframe3 = dataframe + dataframe2

print(dataframe3)

print(dataframe3[dataframe3 >= 0 ])

