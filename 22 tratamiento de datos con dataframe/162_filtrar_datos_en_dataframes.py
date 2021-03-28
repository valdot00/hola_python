# filtrar datos en dataframes

import pandas as pd

import numpy as np

lista_valores = np.random.rand(10,3)

print(lista_valores)

dataframe = pd.DataFrame(lista_valores)

print(dataframe)

columna = dataframe[0] 

print(columna)

print(columna[columna > 0.40])

print(dataframe[dataframe > 0.40])