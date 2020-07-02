#listas

colores=["rojo","amarillo","verde"]

print(colores)

print(colores[0])

print(colores[1])

print(colores[2])

colores[1]="azul"

print(colores[1])

#len()-para saber la cantida de elementos en un arry

print(len(colores))

#.append() - para agregar un nuevo elemento al arry

colores.append("naranja")

print(colores)

#.remove() - para borrar un elemento del arry

colores.remove("rojo")

print(colores)

for color in colores:
    print(color)

#.clear() para limpiar el arry

colores.clear()

print(colores)



