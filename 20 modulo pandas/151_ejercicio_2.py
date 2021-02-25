# ejercicio 2

# dado el fichero exel que os adjunto en varios formatos
# copiar los datos al protapapeles
# crear un dataframe "datos" con esos datos copiados
# mostrar por pantalla, todos los datos del dataframe
# mostar todos los nombres de columnas del dataframe
# mostrar la primera file del dataframe
# mostrar la primera columna del dataframe
# mostrar todas las filas pero solo las columnas "continente" y "poblacion"
# mostrar las primeras 3 filas del dataframe
# mostrar las 2 ultimas filas del dataframe

import pandas as pd

datos = pd.read_clipboard()

print(datos)

print(datos.columns)

print(datos['Superficie'])

print(datos.loc[0])

print(datos.loc[0:3,['Continente','Poblacion']])

print(datos.head(3))

print(datos.tail(2))