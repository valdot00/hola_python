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

# display de los resultados

pantalla = Entry(ventana,font=("arial",20,"bold"), borderwidth=2)
pantalla.grid(row=0,column=0,columnspan=3,pady=10,padx=5)

# boton de reiniciar operacion

boton_reset = Button(ventana,text="AC",width=8,height=2,command=lambda:borrar())
boton_reset.grid(row=0,column=3,pady=10)

ventana.mainloop()
