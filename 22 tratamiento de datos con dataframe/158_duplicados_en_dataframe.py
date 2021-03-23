# eliminar duplicas en dataframes

import pandas as pd

lista_valores = [[1,2],[5,6],[5,8]]

print(lista_valores)

lista_indices = list('mnop')

print(lista_indices)

lista_columnas = ['valor','valor2']

print(lista_columnas)

dataframe = pd.DataFrame(lista_valores, index=lista_indices, columns=lista_columnas)

print(dataframe)

dataframe2 = dataframe.drop_duplicates()

print(dataframe.drop_duplicates())

print(dataframe2.drop_duplicates(['valor1']))