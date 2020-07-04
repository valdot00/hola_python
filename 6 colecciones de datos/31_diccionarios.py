#31 diccionarios

diccionario_colores = {"red":"rojo","blue":"azul","yellow":"amarillo" }

print(diccionario_colores)

print(diccionario_colores["red"])

valor=diccionario_colores["yellow"]

print(valor)

#para agregar un elementoal diccionario

diccionario_colores["black"]="negro"

print(diccionario_colores)

#para borrar un valor

diccionario_colores.pop("yellow")

print(diccionario_colores)

#para borrar el elemento y la clave del()

del(diccionario_colores["black"])

print(diccionario_colores)

for color in diccionario_colores:
    print(color)

for clave,valor in diccionario_colores.items():
    print(clave,valor)    