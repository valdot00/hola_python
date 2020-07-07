#palindroma

print("dame una palabra")

palabra=input()

palabra2=palabra[::-1]

if palabra2==palabra:print("es un palindromo {} = {}".format(palabra2,palabra))
else:print("NO es un palindromo {} = {}".format(palabra2,palabra))

print("------------------------------")

# Imprime en ese caso "Es palindroma"
if palabra == palabra[::-1]:
    print("Es palindroma")
else:
    print("No es palindroma")

print("------------------------------")

# En este caso imprime "Es Palindroma"
if palabra == ''.join(reversed(palabra)):
    print("Es Palindroma")
else:
    print("No es Palindroma")




   



     







 
            
        
   



      





