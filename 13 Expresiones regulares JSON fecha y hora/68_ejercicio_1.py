#68 ejercicio 1

#crea una funcion "buscar" que mediante una exprecion regular indique
#si una palabra esta en una frase
#probar la funcion "buscar con estas frases"
#texto = "esto es una frase pruebas para hacer busquedas"
#palabra_a_buscar = "frase"
#en caso de encontrar la palabra en la frase, indica en que posicion 
#y en cual dinaliza

import re

def buscar(palabra,texto):
    resultado = re.search(palabra,texto)
    return resultado

texto = "esto es una frase de pruebas para hacer busquedas" 
palabra = "frase"

resultado = buscar(palabra,texto)

if(resultado):
    print("palabra {} encontrada".format(palabra))
    inicial = resultado.start()
    final = resultado.end()
    print("empieza en la posicion {} y finaliza en la posicion {}".format(inicial,final))
else:
    print("palabra {} no encontrada".format(palabra))