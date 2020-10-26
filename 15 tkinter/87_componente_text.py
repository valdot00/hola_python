#tkinter - componente text (campo de texto, de varias lineas, para introducir texto por teplado)

import tkinter

raiz = tkinter.Tk()
raiz.title("componente text")

#creamos el componente text (texto largo de varias lineas)

entrada = tkinter.Text(raiz)
entrada.config(width=20, height=10, font=("Verdana",15), padx=10, pady=10, fg="green", selectbackground="lightgrey")
entrada.pack()

raiz.mainloop()