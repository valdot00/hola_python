# agrupacion en dataframes

import pandas as pd
from pandas.core.frame import DataFrame

import numpy as np

lista_valores = {'clave1':['x','x','y','y','z'],
                 'clave2':['a','b','a','b','a'],
                 'datos1':np.random.rand(5),
                 'datos2':np.random.rand(5)}

print(lista_valores)

dataframe = pd.DataFrame(lista_valores)

print(dataframe)

grupo1 = dataframe['datos1'].groupby(dataframe['clave1'])

print(grupo1)

print(grupo1.mean())