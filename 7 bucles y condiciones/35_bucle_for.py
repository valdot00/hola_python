#35 bucle for

colores=["rojo","verde","azul"]

for color in colores:
    print(color)

print("----------")    

cadena="hola mundo"

for caracter in cadena:
    print(caracter)

print("----------")       

range(8)

print(range(8))

print("----------")    

for numero in range(8):
    print(numero)

print("----------")        

for numero in range(3,8):
    print(numero)

print("----------")        

for numero in range(3,8,2):
    print(numero)

print("----------")            

#break-para parar el bucle

for numero in range(10):
    if(numero==5):
       break
print(numero)

print("----------")    

#continue - para parar solo la interaccion actual

for numero in range(10):
    if(numero==6):
        continue
    print(numero)

print("----------")    

#for doble

for numero1 in range(4):
    for numero2 in range(3):
        print(numero1,numero2)    

print("----------")    