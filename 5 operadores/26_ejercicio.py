#26 ejercicio 1

#crear una variable "nota1" que tenga el valor 6
#crear otra variable "nota2" que tenga el valor 4
#crear otra variable "nota3" que tenga el valor 7
#crear otra variable "nota_media" que tenga el valor medio de las 3 notas anteriores
#crear otra variable "nota final" que tenga el valor "aprobado" {mayor o igual a 5}

nota1=6
nota2=4
nota3=7

nota_media=(nota1+nota2+nota3)/3

print(nota_media)

if(nota_media >= 5):
   nota_final="aprobado"

print("{}".format(nota_final))   

