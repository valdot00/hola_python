# tkinter - messagebox para realizar una pregunta

import tkinter
from tkinter import messagebox

raiz = tkinter.Tk()
raiz.title("messagebox 2")

# crear una ventana para preguntar o confirmar algo

# definimos la funcion

def preguntar():
    resultado = tkinter.messagebox.askquestion("titulo de la pregunta","¿quieres borrar este fichero?")
    if (resultado == "yes"):
        print("si, quiero borrar el fichero")
    else:
        print("no, quiero borrar el fichero")    

boton = tkinter.Button(raiz,text="pulsar para preguntar",command=preguntar)
boton.pack()

raiz.mainloop()