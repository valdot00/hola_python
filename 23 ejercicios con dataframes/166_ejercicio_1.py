# ejerccio  

#vamos a filtar datos en un dataframe

#crearemos una lista de 50 valores aleatorios enteros entre los valores 0 y 100
#convertiremos esta lista en un dataframe con 5 filas y 10 columnas
#filtaremos los datos del dataframe para visualizar solo los valores que sean mayores de 50

import pandas as pd
from pandas.core.frame import DataFrame

import numpy as np

lista_valores = np.random.randint(0,100,50)

print(lista_valores)

print(lista_valores.resize(5,10))

print(lista_valores)

dataframe = pd.DataFrame(lista_valores)

print(dataframe)

print(dataframe[dataframe>50])