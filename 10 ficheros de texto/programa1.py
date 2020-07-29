#56

import moduloficheros

nombre_fichero='fichero1.txt'
fichero = moduloficheros.Fichero(nombre_fichero)

texto = "esta es la primera linea del fichero.\nEsta es sera la segunda linea"
fichero.grabar_fichero(texto)

texto='\neste es un texto incluido en la tercera fila'
fichero.incluir_fichero(texto)

texto_leido = fichero.leer_fichero()
print(texto_leido)

