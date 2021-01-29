#dataframes

import pandas as pd

import webbrowser
website = 'https://es.wikipedia.org/wiki/anexo:campeones_de_la_NBA'
webbrowser.open(website)

dataframe_nba = pd.read_clipboard()

print(dataframe_nba)

print(dataframe_nba.columns)

print(dataframe_nba['campeon del oeste'])#muestra a campeon del oeste

print(dataframe_nba.loc[5])#muestra el quinto de la tabla

print(dataframe_nba.head(3))#muestra los primeros 3 de la tabla

print(dataframe_nba.tail(2))#muestra los ultimos datos de la tabla

lista_asignaturas = ['matematicas','historia','fisica']
lista_notas = [8,7,9]
diccionario = {'asignatura':lista_asignaturas,'nota':lista_notas}

print(diccionario)

dataframe_nota = pd.DataFrame(diccionario)

print(dataframe_nota)





