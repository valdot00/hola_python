#tkinter - componente button (boton)

import tkinter

raiz = tkinter.Tk()
raiz.title("componente button")

#crearemos el componente button (boton, para ejecutar una accion se pulsa)

def accion():
    print("hola boton")

boton = tkinter.Button(raiz, text="ejecutar", command=accion)
boton.config(fg="green")
boton.pack()

raiz.mainloop()
