#44 ejercicio 
#crear una clase "coche" que tenga estos atributos:
#marca, color, combustible y cilindrada

#crear otra funcion "_init_" que asigna parametros 
# de la clase a los a tributos de la clase

#crar otra funcion "mostrar_caracteristicas" que mediante
#print muestre por pantalla las caracteristicas (o atributos)
#que tiene el coche

#crear un objeto "coche1" de la clase "coche" con los atributos
#"opel","rojo","gasolina","1.6"

#ejecutar la funcion "mostrar_caracteristicas" del objeto "coche1"

class coche:
    def __init__(auto,marca,color,combustible,cilindrada):
        auto.marca=marca
        auto.color=color
        auto.combustible=combustible
        auto.cilindrada=cilindrada

    def mostrar(auto):
        print("caracteristicas del coche marca:{} color:{} combustible:{} cilindrada:{}"
        .format(auto.marca,auto.color,auto.combustible,auto.cilindrada))

coche1=coche("opel","rojo","gasolina","1.6")

#print(coche1.color)

print(coche1.mostrar())