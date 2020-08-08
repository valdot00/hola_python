#60 ejercicio 1

#crear el diccionario "frutas"

#gravar esta estructura de datos "frutas" en un fichero binario
#"fichero.pckl"
#ya que en un fichero de texto, solo se guadan caracteristicas,
#pero no se
#puede guardar estas estructuras

#repupera esta escrutura de datos del fichero "fichero.pckl"
#verifica que sigue siendo un diccionario,
#ejecutando el metodo .values()

frutas={"manzana":"apple","naranja":"orange","platano":"banana","limon":"lemon"}

print(frutas.values())

#dict_values(['apple','orange','banana','lemon'])

fichero = open("fichero1.pckl","wb")

import pickle

pickle.dump(frutas,fichero)

fichero.close()

fichero2 = open("fichero1.pckl","rb")

datos = pickle.load(fichero2)

print(datos)

datos.values()

print(datos.values())
