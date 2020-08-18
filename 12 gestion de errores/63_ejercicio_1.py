#63 ejercicio 1
# crear una funcion "operacion" que dados 3 numeroes, divida el primer
#numero entre la resta de los otros dos numeroes
#utiliza la funcion creada con los numeroes 5,4,2
#utiliza la funcion creada con los numeroes 6,3,3
#utiliza el bloque try... except para controlar cuaklquier 
#posible error

def operacion(numero1,numero2,numero3):
    resultado = numero1 / (numero2 - numero3)
    return resultado

numero1 = 5
numero2 = 4
numero3 = 2

resultado =operacion(numero1,numero2,numero3)

print(resultado)

print("-------")

numero1 = 6
numero2 = 3
numero3 = 3

try:
    resultado =operacion(numero1,numero2,numero3)
    print(resultado)
except:
    print("error. los ultimos dos numeros tienen que ser diferentes")