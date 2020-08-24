#65 expresiones regulares (search findall, split, sub)

texto = "hola mi nombre es jorge oswaldo pelayo arellano"

import re

re.search("nombre",texto)

print(re.search("nombre",texto))

re.search("hola",texto)

print(re.search("hola",texto))

resultado = re.search("nombre",texto)

if(resultado):
    print("cadena encontrada")
else:
    print("cadena No encontrada")

re.search("jorge$",texto) #busca al final del texto

print(re.search("jorge$",texto))

re.search("^jorge",texto) #busca al inicio del texto

print(re.search("^jorge",texto))

re.search("mi.*es",texto) #para buscar un patron en una cadena

print(re.search("mi.*es",texto))

#findall

texto = """ el coche de luis es rojo,
            el coche de antonio es blanco,
            y el coche de maria es rojo
        """  

re.findall("coche.*rojo",texto)

print(re.findall("coche.*rojo",texto))

#split 

texto = "la silla es blanca y vale 80"

re.split("\s",texto)

print(re.split("\s",texto))

#sub 

texto = "la silla es blanca y vale 80"

re.sub("blanca","roja",texto)

print(re.sub("blanca","roja",texto))