# filter - funcion para filtrar resultados segun una condicion  

def positivo(numero):
    if(numero > 0):
        return True
    else:
        return False

positivo(5)

print(positivo(5))

print(positivo(-5))

numeros = [4,-2,8,-5,-3,9,1,-7]

filtro = filter(positivo,numeros)

resultado = list(filtro)

print(resultado)