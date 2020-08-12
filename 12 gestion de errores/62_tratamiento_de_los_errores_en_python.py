#62 tratamiento de los errores en python

#try...except...else...finally

#numero1 = 5
#numero2 = 0
#division = numero1/numero2

try:
    numero1=5
    numero2=0
    division=numero1/numero2
    print(division)
except:
    print("ha habido un error")   

#zeroDivisionError

try:
    numero1=5
    numero2=2
    division=numero1/numero2
    print(division)
except zeroDivisionError:
    print("Error, division entre cero")
except:
    print("ha habido un error")
else:
    print("la division funciono correctamente")  

#finally

try:
    numero1=5
    numero2=2
    division=numero1/numero2
    print(division)
except zeroDivisionError:
    print("Error, division entre cero")
except:
    print("ha habido un error")
else:
    print("la division funciono correctamente")  
finally:
    print("esta prueba del try se ha acabado")    


