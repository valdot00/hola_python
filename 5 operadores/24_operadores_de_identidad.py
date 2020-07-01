#operadores de identidad (is, is not)

frutas=["manzana","pera"]
frutas2=["manzana","pera"]
frutas3=frutas

x=(frutas3 is frutas)

print(x)

print(frutas3 is frutas)

frutas3.append("naranja") #para agregar una elemento a un arreglo

print(frutas3)

#is not 

frutas3 is not frutas

print(frutas3 is not frutas)

