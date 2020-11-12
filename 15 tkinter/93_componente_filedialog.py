# tkinter - filedialog para abrir un fichero

import tkinter
from tkinter import filedialog

raiz = tkinter.Tk()
raiz.title("filedialog")

#

def abrirfichero():
    rutafichero = filedialog.askopenfilename(title="abrir un fichero")

boton = tkinter.Button(raiz,text="pulsa para empezar",command=abrirfichero)
boton.pack()

raiz.mainloop()