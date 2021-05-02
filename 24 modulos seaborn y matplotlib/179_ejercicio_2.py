#ejercicio

#crear una arry con 100 numeros enteros aleatorios con valores comprendidos entre 0 y 500
#utilizar un diagrama de caja para represebntar los valores aleatorios generados

import numpy as np
import seaborn as sns

datos = np.random.randint(0,500,100)#genera 100 elementos con un valor de 0 a 500

print(datos)

print(sns.boxplot(datos))