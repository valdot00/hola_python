# ejercicio 2

#obtener la tabla de paises de la paguina 'https://es.wikipedia.org/wiki/anexo:pa%c3%aDses'
#limpiar los datos lo necesario para que los nombres de la columnas sean correctos.

import pandas as pd

excel = pd.ExcelFile('\Users\PC\Desktop\jorge_oswaldo_pelayo_arellano\python\21 HTML Y EXCEL\poblacin.xls')

dataframe = excel.parse('Hoja 1')

print(dataframe)

print(dataframe['ciudad mas poblada'][3])

fichero_csv = pd.read_csv('\Users\PC\Desktop\jorge_oswaldo_pelayo_arellano\python\21 HTML Y EXCEL\poblacin.csv')

print(fichero_csv)

print(fichero_csv['ciudad mas poblada'][1])