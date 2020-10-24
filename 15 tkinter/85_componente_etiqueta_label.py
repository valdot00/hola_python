#tkinter - componente label

import tkinter

raiz = tkinter.Tk()
raiz.title("componente etiqueta (label)")

#creamos el componente label (etiqueta)

texto = "hola label"
etiqueta = tkinter.Label(raiz,text=texto)
etiqueta.config(fg="green",bg="lightgrey",font=("Cortana",30))
etiqueta.pack()

raiz.mainloop()