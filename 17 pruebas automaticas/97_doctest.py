# Doctest - generar pruebas dentro de la documentacion

def sumar(numero1,numero2):
    """
    esto es la documentacion de esta funcion 
    recibe dos numeros como parametros y devuelve su suma

    >>> sumar(4,3)
    7

    >>> sumar(5,4)
    9

    >>> sumar(1,3)
    7

    """
    return numero1 + numero2

resultado = sumar(2,4)
print(resultado)

import doctest
doctest.testmod()
