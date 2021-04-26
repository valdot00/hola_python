#crear una lista de 1000 valores aleatorios que sigan una distribucion normal
#crear un histograma mediante matplotlib con la lista de valores
#crear un diagrama de caja (donde se acumula el 50% de los valores) mediante seaborn

import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns

lista_valores = np.random.randn(1000)

print(lista_valores)

print(ptl.hist(lista_valores))

print(sns.boxplot(lista_valores))