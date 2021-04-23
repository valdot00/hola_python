#diagrama de caja

#sirve para representar graficamente una serie de datos numericos a traves de sus cuartiles

import pandas as pd

import numpy as np

import matplotlib as mpl

import seaborn as sns

%mpl inline

datos = np.random.randn(100)

print(datos)

print(sns.boxplot(datos))