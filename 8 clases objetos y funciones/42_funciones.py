#42 funciones

def saludar():
    print("buenos dias")

print(saludar())

print("-----------")

def saludar(nombre):
    print("buenos dias "+nombre)

nombre = "antonio"    

print(saludar(nombre))

print("-----------")

def sumar(numero1,numero2):
    suma=numero1+numero2
    return suma

numero1=5

numero2=3

resultado=sumar(numero1,numero2)

print(resultado)

print("-----------")

#paso de valor por referencia

colores=["rojo","verde","azul"]

def incluir_color(colores,color):
    colores.append(color)

color = "negro"

incluir_color(colores,color)

print(colores)    

print("-----------")