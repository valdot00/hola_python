#50 ejercicio

#crear un modulo "modulo1.py"
#añadir la clase "coche" crada en el ejercicio anterior al modulo "modulo1"
#añadir la funcion lambda "media" creada en un ejercicio anterior al modulo "modulo1"

#crear un programa en python "programa1.py"
#iportar el modulo "modulo1" antes creado
#crear un objeto "coche1" al instalar la clase "coche"
#mediante print mostrar las caractaristicas del coche
#calcular la media de 3 notas y mostar el resultado con print

#ejecutar el programa "programa.py" y ver el resultado

class coche:
    def __init__(auto,marca,color,combustible,cilindrada):
        auto.marca=marca
        auto.color=color
        auto.combustible=combustible
        auto.cilindrada=cilindrada

    def mostrar(auto):
        print("caracteristicas del coche marca:{} color:{} combustible:{} cilindrada:{}"
        .format(auto.marca,auto.color,auto.combustible,auto.cilindrada))

media=lambda nota1,nota2,nota3 : (nota1+nota2+nota3)/3 

