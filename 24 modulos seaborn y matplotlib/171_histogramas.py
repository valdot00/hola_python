# seaborn - graficos estadisticos

import pandas as pd
import numpy as np

import matplotlib as mpl
import seaborn as sns

%matplotlib inline

datos1 = np.random.randn(100)

print(datos1)

print(mpl.pyplot.hist(datos1))#grafica de los datos anteriores

print(sns.distplot(datos1,color="green")#grafica de curvas

print(mpl.pyplot.hist(datos1,color="gray",alpha=0.5))

datos2 = np.randon.randn(100)

print(mpl.pyplot.hist(datos2,color="yellow",alpha=0.4))

print(mpl.pyploy.hist(datos1,color="green",alpha=0.3,bins=20,density=True))

print(mpl.pyploy.hist(datos2,color="blue",alpha=0.3,bins=20,density=True))

datos3 = np.random.randn(1000)

datos4 = np.random.randn(1000)

print(sns.jointplot(datos3,datos4))#grafica de puntos

print(sns.jointplot(datos3,datos4,kind="hex"))