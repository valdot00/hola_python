#agregacion (operaciones que dan un valor, como la media)

from typing import List

import pandas as pd

import numpy as np

lista_valores = [[1,2,3],[4,5,6],[7,8,9],[np.nan,np.an,np.nan]]

print(lista_valores)

lista_columnas = list('abc')

print(lista_columnas)

dataframe = pd.DataFrame(lista_valores, columns=lista_columnas)

print(dataframe)

print(dataframe.agg(['sum','min']))

print(dataframe.agg('sum',axis=1))