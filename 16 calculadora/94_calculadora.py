from tkinter import *

ventana = Tk()
ventana.title("calculadora")
ventana.geometry("400x600")
ventana.resizable(False,False)
ventana.configure(background="gray")

# Funciones

operacion = ""
resultado = StringVar()

def borrar():
    global operacion
    global resultado
    operacion = ""
    pantalla.delete(0,END)

def pulsar(valor):
    global operacion
    global resultado
    operacion = operacion + str(valor)
    pantalla.delete(0,END)
    pantalla.insert(0,operacion)    

# display de los resultados

pantalla = Entry(ventana,font=("arial",20,"bold"), borderwidth=2)
pantalla.grid(row=0,column=0,columnspan=3,pady=10,padx=5)

# boton de reiniciar operacion

boton_reset = Button(ventana,text="AC",width=8,height=2,command=lambda:borrar())
boton_reset.grid(row=0,column=3,pady=10)

# botones de la primera fila

ancho = 8
alto = 3

boton1=Button(ventana,text="1",width=ancho,height=alto,command=lambda:pulsar("1"))
boton1.grid(row=1,column=0,padx=5,pady=5)

boton2=Button(ventana,text="2",width=ancho,height=alto,command=lambda:pulsar("2"))
boton2.grid(row=1,column=1,padx=5,pady=5)

boton3=Button(ventana,text="3",width=ancho,height=alto,command=lambda:pulsar("3"))
boton3.grid(row=1,column=2,padx=5,pady=5)

boton4=Button(ventana,text="4",width=ancho,height=alto,command=lambda:pulsar("4"))
boton4.grid(row=1,column=3,padx=5,pady=5)

ventana.mainloop()
