#52 leer ficheros

#leer el fichero de texto

fichero = open("ficherotexto.txt","rt")

datos_fichero = fichero.read()

print(datos_fichero)