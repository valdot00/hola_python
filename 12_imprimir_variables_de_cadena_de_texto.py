#12 imprimir variables de cadena de texto

nombre="jorge"
print("--------------------------------------")

print("buenos dias " + nombre)

print("--------------------------------------")
# .format
edad = 28
print("buenos dias {}, feliz {} cumpleaños".format(nombre,edad))

print("--------------------------------------")
resultado=10/3
print(resultado)
print("--------------------------------------")
print("el resultado es {r}".format(r=resultado))

print("--------------------------------------")

print("el resultado es {r:1.3f}".format(r=resultado))#para menos desimales

print("--------------------------------------")
#f-strings
print(f"buenos dias {nombre}, feliz {edad} cumpleños")
print("--------------------------------------")