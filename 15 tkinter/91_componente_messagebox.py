# tkinter - componente messagebox (mostrar informacion)

import tkinter
from tkinter import messagebox

raiz = tkinter.Tk()
raiz.title("messagebox")

#creamos componente "popup" (ventana de informacion)
def avisar():
    tkinter.messagebox.showinfo("titulo","mensaje con la informacion")

boton = tkinter.Button(raiz,text="pulsar para aviso",command=avisar)
boton.pack()

raiz.mainloop()