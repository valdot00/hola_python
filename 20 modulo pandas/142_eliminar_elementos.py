# eliminar elementos en series y dataframe

import pandas as pd
import numpy as np

#np.arange(3) crea una array del 0 al 2

print(np.arange(4))

serie = pd.Series(np.arange(4),index=['a','b','c','b'])

print(serie)

#serie.drop('c') para eliminar un valor de la serie

print(serie.drop('c'))

lista_valores = np.arange(9).reshape(3,3)

lista_indices = ['a','b','c']
lista_columnas =['c1','c2','c3']
dataframe = pd.DataFrame(lista_valores, index=lista_indices,columns=lista_columnas)

print(dataframe)

print(dataframe.drop('b'))#para borrar el indice b

print(dataframe.drop('c2',axis=1))#para borrar la columna c2

dataframe = dataframe.drop('b')

print(dataframe)

