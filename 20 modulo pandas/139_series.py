# series

import pandas as pd

serie1 = pd.Series([3,5,7])

print(serie1)

serie1[1]

print(serie1[1])

asignaturas = ['matematicas','historia','fisica','literatura']
notas = [8,6,9,7]
serie_notas_daniel = pd.Series(notas,index=asignaturas)

print(serie_notas_daniel)

print(serie_notas_daniel['fisica'])

print(serie_notas_daniel[serie_notas_daniel >= 8])

serie_notas_daniel.name = 'nota de daniel'

print(serie_notas_daniel)

dicionario = serie_notas_daniel.to_dict()

print(dicionario)

serie = pd.Series(dicionario)

print(serie)

asignaturas = ['matematicas','historia','fisica','literatura']
notas_ana = [7,8,5,9]
serie_notas_ana = pd.Series(notas_ana,index=asignaturas)

print(serie_notas_ana)

serie_notas_clase = (serie_notas_daniel+serie_notas_ana)/2

print(serie_notas_clase)