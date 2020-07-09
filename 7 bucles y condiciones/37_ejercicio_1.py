#37 ejercicio 1

#crea un dicionario con los siguientes pares de valores
#manzana apple
#naranje orange
#platano banana
#limon lemon

#muestra la traducion para la palabra "naranja"
#añade un elemento nuevo "piña" y pineaple"
# haz un bucle para mostrar todos los elementos del dicionario

diccionario={"manzana":"apple","naranja":"orange","platano":"banana","limon":"lemon"}

print(diccionario["naranja"])

print("-----------")

diccionario["piña"]="pineapple"

print(diccionario)

print("-----------")

for clave,valor in diccionario.items():
        print("{} en ingles es {}".format(clave,valor))
        print("---------------------")
