#indices

import pandas as pd

lista_valores = [1,2,3]
lista_indices = [a,b,c]
serie = pd.Series(lista_valores,index=lista_indices)

print(serie)

print(serie.index[0])

serie.index[0] = 'z'

lista_valores = [[6,7,8],[8,9,5],[6,9,7]]

lista_indices = ['matematicas','historia','fisica']
lista_nombre = ['antonio','maria','pedro']

dataframe = pd.DataFrame(lista_valores, index=lista_indices,columns=lista_nombre)

print(dataframe)

print(dataframe.index)

print(dataframe.index[2])
