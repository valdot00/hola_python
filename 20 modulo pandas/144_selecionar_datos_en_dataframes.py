# seleccionando entrada para dataframe

import pandas as pd
import numpy as np

lista_valores = np.arange(25).reshape(5,5)

print(lista_valores)

lista_indices = ['i1','i2','i3','i4','i5']

lista_columnas = ['c1','c2','c3','c4','c5']

datafreme = pd.DataFrame(lista_valores, index=lista_indices,columns=lista_columnas)

print(datafreme)

print(datafreme['c2'])

print(datafreme['c2']['i2'])

print(datafreme[['c3','c4']])

print(datafreme[['c2','c3','c4']])

print(datafreme)

print(datafreme[datafreme['c2']>15])

print(datafreme>20)

print(datafreme.loc['i3'])

print(datafreme.loc['i3']['c4'])