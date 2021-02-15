# valores nulos - NaN

import pandas as pd
import numpy as np

lista_valores = ['1','2',np.nan,'4']

print(lista_valores)

serie = pd.Series(lista_valores, index=list('abcd'))

print(serie)

print(serie.isnull())

print(serie.dropna())

print(serie)

lista_valores = [[1,2,3],[4,np.nan,5],[6,7,np.nan]]

print(lista_valores)

lista_indices = list('123')

print(lista_indices)

lista_columnas = list('abc')

dataframe = pd.DataFrame(lista_valores,index=lista_indices,columns=lista_columnas)

print(dataframe)

print(dataframe.isnull())

print(dataframe.dropna())

print(dataframe)

print(dataframe.fillna(0))