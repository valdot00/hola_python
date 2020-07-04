#31 diccionarios

diccionario_colores = {"red":"rojo","blue":"azul","yellow":"amarillo" }

print(diccionario_colores)

print("----------------------------------------------------")

print(diccionario_colores["red"])#clave "red" con valor "rojo"

print("----------------------------------------------------")

valor=diccionario_colores["yellow"]#clave "yellow" con valor amarillo

print(valor)

print("----------------------------------------------------------------------")

#para agregar un elementoal diccionario

diccionario_colores["black"]="negro"#agregando clave "black" con valor "negro"

print(diccionario_colores)

print("----------------------------------------------------------------------")

#para borrar un valor

diccionario_colores.pop("yellow")#borra "yellow" con el valor "amarillo"

print(diccionario_colores)

print("----------------------------------------------------")

#para borrar el elemento y la clave del()

del(diccionario_colores["black"])

print(diccionario_colores)

print("----------------------------------------------------")

for color in diccionario_colores:
    print(color)#para imprimir las claves del diccionario

print("----------------------------------------------------")

for clave,valor in diccionario_colores.items():
    print(clave,valor)#para imprimir la clave y el valor del diccionario    

print("----------------------------------------------------")