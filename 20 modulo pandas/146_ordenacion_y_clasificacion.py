# ordenar y clasificar series

import pandas as pd
import numpy as np

print(range(4))

lista_valores = range(4)

lista_indices = list('CABD')

print(lista_indices)

serie = pd.Series(lista_valores, index=lista_indices)

print(serie)

print(serie.sort_index()) #ordena la serie por el index

print(serie.sort_values()) #los ordena por los valores

print(serie.rank()) #los ordena por un ranking

serie2 = pd.Series(np.random.randn(10))

print(serie2)

print(serie2.rank())

print(serie2.sort_values()) # de menor valor a mayor

print(serie2.sort_index())