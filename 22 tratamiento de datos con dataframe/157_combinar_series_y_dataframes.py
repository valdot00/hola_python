# combinacion series y dataframes

import pandas as pd

import numpy as np

serie1 = pd.Series([1,2,np.nan])

print(serie1)

serie2 = pd.Series([4,5,6])

print(serie2)

serie3 = serie1.combine_first(serie2)

print(serie3)

lista_valores = [1,2,np.nan]

dataframe1 = pd.DataFrame(lista_valores)

print(dataframe1)

lista_valores_2 = [4,5,6]

dataframe_2 = pd.DataFrame(lista_valores_2)

print(dataframe_2)

dataframe_3 = dataframe1.combine_first(dataframe_2)

print(dataframe_3)