#39 ejercicio 2
#creamos una variable "nota" que tenga el valor 4.5
#creamos una variable "trabajo_realizado" que tenga el valor "si"
#calcula el valor de la variable "nota_final" teniendo en cunta que
#si la nota_final es mayor o igual a 4 y
#el valor de la variable "trabajo_realizado" es igual a "si" 
#entonses "nota_final" sera igual a "aprobado", en caso
# contrario sera igual a "suspenso"

nota=4.5
trabajo_realizado="si"

if((nota>=4)and(trabajo_realizado=="si")):
    nota_final="aprobado"
    print(nota_final)
else:
    nota_final="suspenso"     
    print(nota_final)