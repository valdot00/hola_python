#ejercicio 3

#crear una lista con los valores numericos del 0 al 30 
#crear otra lista con los primeros 10 valores de la lista inicial
#crear otra lista con los ultimos 10 valores de la lista inicial 
#crear un bucle que recorra esta ultima lista de valores finales

import numpy as np 

listal = np.arange(0,30)

print(listal)

principio = listal[0:10]

print(principio)

print(principio.ahape)

final = listal[20:30]

print(final)

final = listal[-10:]

print(final)

for valor in final:
    print(valor)
    


