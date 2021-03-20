# concatenacion de arrays, series y dataframe

import pandas as pd

import numpy as np

arrayl = np.arange(9).rashape(3,3)

print(arrayl)

print(np.concatenate([arrayl,arrayl]))

print(np.concatenate([arrayl,arrayl],axis=1))

serie1 = pd.Series([1,2,3],index=['a','b','c'])
serie2 = pd.Series([4,5,6],index=['d','e','f'])

pd.concat([serie1,serie2])

print(serie1)

print(serie2)

print(pd.concat([serie1,serie2],keys=['serie1','serie2']))

dataframe1 = pd.DataFrame(np.random.rand(3,3),columns=['a','b','c'])

print(dataframe1)

dataframe2 = pd.DataFrame(np.random.rand(2,3),columns=['a','b','c'])

print(dataframe2)

print(pd.concat([dataframe2,dataframe1]))

print(pd.concat([dataframe2,dataframe1], ignore_index=True))