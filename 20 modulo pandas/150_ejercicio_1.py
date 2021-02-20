# ejercicio

# tenemos 3 clases "clase1","clase2","clase3"
# vamos a generar un numero aletorio de alumnnos por clase
# para obtener un numero aleatorio utilizaremos
# np.random.randint(minimo,maximo,numero)

# crear una serie de clases y alumnos
# utilizar el indice de la serie creada para saber el numero 
# de alumnos de la clase2

import pandas as pd
import numpy as np

minimo = 10
maximo = 40
numero = 3
alumnos = np.random.randint(minimo,maximo,numero)

print(alumnos)

clases = ['clase1','clases2','clase3']

serie = pd.Series(alumnos,index=clases)

print(serie)