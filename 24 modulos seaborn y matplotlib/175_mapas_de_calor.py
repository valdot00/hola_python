#mapas de calor (heatmap)

#https://seaborn.pydata.org/generated/seaborn.heatmap.html

import pandas as pd 

import numpy as np

import seaborn as sns
%matplotlib inline

vuelos = sns.load_dataset('flights')

print(vuelos.head())

vuelos = vuelos.pivot('month','year','passengers')

print(sns.heatmap(vuelos))

print(sns.heatmap(vuelos,annot=True,fmt='d'))

valor_central = vuelos.loc['may'][1956]

print(valor_central)

print(sns.heatmap(vuelos,center=valor_central,annot=True,fmt='d'))

print(sns.heatmap(vuelos,center=valor_central,annot=True,fmt='d',cbar_kws={'orientation':'horizontal'}))


