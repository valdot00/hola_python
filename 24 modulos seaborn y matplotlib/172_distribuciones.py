#combinar estilos

import pandas as pd

import numpy as np

import matplotlib as mpl

import seaborn as sns

%mpl inline

datos = np.random.randn(100)

print(datos)

print(sns.distplot(datos,color="gray"))

print(sns.distplot(datos,color="green",rug=False,hist=False))

argumentos_curva = {'color':'black','label':'curva'}

argumentos_histograma = {'color':'gray','label':'histograma'}

print(sns.distplot(datos,bins=25,kde_kws=argumentos_curva,hist_kws=argumentos_histograma))

serie = pd.Series(datos)

print(serie)

print(sns.distplot(serie,bins=25,color="green"))