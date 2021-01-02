#ejercicio 

#apartir de la lista "numeros" que contiene numeros del 1 al 10
#obtener mediante "filter" una lsita denominada "pares" con los 
#numeros pares de la lista "numeros"

numeros = [1,2,3,4,5,6,7,8,9,10]

def par(numero):
    if(numero % 2)==0:
        return True
    else:
        return False

print(par(5))

print(par(10)) 

resultado = filter(par,numeros)

pares = list(resultado)

print(pares)
