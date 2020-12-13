# map - aplicar una funciones a una lista

def multiplicar(numero):
    return numero * 2

print(multiplicar(2))

numeros = [2,4,6]

# map(la funcion, la lista de numeros que usa la funcion)

mapeo = map(multiplicar,numeros)

print(mapeo)

resultado = list(mapeo)

print(resultado)

#-----------------------------------------------

lista_resultado = list(map(multiplicar,numeros))

print(lista_resultado)

#-----------------------------------------------

lista_resultado = list(map(lambda numero: numero * 2,numeros))

print(lista_resultado)

#-------------------------------------------------------------