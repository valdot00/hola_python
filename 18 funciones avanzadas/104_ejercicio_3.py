#ejercicio

#a partir de una lista de numeros del 1 al 10,
#optener una nueva lista con todos los elementos incrementados en 10 unidades

numeros = [1,2,3,4,5,6,7,8,9,10]

print(numeros)

def incrementar(numero):
    resultado = numero + 10
    return resultado

print(incrementar(5))

resultado = map(incrementar,numeros)

numeros2 = list(resultado)

print(numeros2)