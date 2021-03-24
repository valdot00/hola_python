# reemplazar datos en series

import pandas as pd

serie = pd.Series([1,2,3,4,5],index=list('abcde'))

print(serie)

print(serie.replace(1,6))

serie = serie.replace(1,6)

print(serie)

serie = serie.replace({2:8,3:9})

print(serie)