# ejercicio 

#lerr el fichero adjunto "poblacion.xlsx" y cargar los datos en un dataframe
#con esos datos, visualizar cual es la ciudad mas popular en america

#leer el fichero adjunto "poblacion.csv" y cargar los datos en un dataframe
#con esos datos, visualizar cual es la ciudad mas poblada en africa

import PANDAS as pd

from pandas.core.frame import DataFrame

excel = pd.ExcelFile('\Users\PC\Desktop\jorge_oswaldo_pelayo_arellano\python\21 HTML Y EXCEL\poblacion.xlsx')

dataframe = excel.parse('Hoja 1')

print(dataframe)

print(DataFrame['ciudad mas poblada'][3])

fichero_csv = pd.read_csv('C:\Users\PC\Desktop\jorge_oswaldo_pelayo_arellano\python\21 HTML Y EXCEL\poblacion.csv')

print(fichero_csv)

print(fichero_csv['ciudad mas poblada'][1])