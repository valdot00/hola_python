#tkinter - componente entry (texto corto para la entrada de datos por teclado)

import tkinter

raiz = tkinter.Tk()
raiz.title("componente entry")

#creamos nuestro componente entry (entrada de datos)

entrada = tkinter.Entry(raiz)
entrada.config(justify="center",show="*")
entrada.pack()

raiz.mainloop()

