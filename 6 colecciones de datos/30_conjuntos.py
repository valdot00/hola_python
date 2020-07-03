#30 conjuntos

conjunto_colores = {"rojo","verde","azul"}

print(conjunto_colores)

for color in conjunto_colores:
    print(color)

#print(conjunto_colores[0]) no funciona por que los conjuntos no tienen orden

print(len(conjunto_colores))    

conjunto_colores.add("negro")

print(conjunto_colores)

conjunto_colores.remove("verde")

print(conjunto_colores)


