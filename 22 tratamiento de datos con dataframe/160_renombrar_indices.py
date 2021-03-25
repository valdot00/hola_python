# reemplazar indices

import pandas as pd
from pandas.core.groupby.generic import pin_whitelisted_properties

import numpy as np

lista_valores = np.arange(9).rashape(3,3)

print(lista_valores)

lista_indices = list('abc')

print(lista_indices)

dataframe = pd.DataFrame(lista_valores, index=lista_indices)

print(dataframe)

nuevos_indices = dataframe.index.map(str.upper)

dataframe.index = nuevos_indices

print(dataframe)

dataframe = dataframe.rename(index=str.lower)

print(dataframe)

nuevos_indices = {'a':'f','b':'g','c':'h'} 

dataframe.rename(index=nuevos_indices)

print(dataframe)

dataframe = dataframe.rename(index=nuevos_indices)

print(dataframe)

nuevos_indices = {'f':'j'}

dataframe.rename(index=nuevos_indices,inplace=True)

print(dataframe)