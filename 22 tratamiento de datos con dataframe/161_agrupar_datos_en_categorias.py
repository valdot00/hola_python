# agrupar datos en categoria

import pandas as pd

import numpy as np

precios = [42,55,48,23,5,22,88,34,26]

rango = [0,10,20,30,40,50,60,70,80,90,100]

precios_con_rango = pd.cut(precios,rango)

print(precios_con_rango)

print(pd.value_counts(precios_con_rango))