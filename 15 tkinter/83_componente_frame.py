#tkinter-componente frame

import tkinter

raiz = tkinter.Tk()
raiz.title("83 COMPONENTE FRAME")

#CREAMOS EL COMPONENTE FRAME

frame = tkinter.Frame(raiz)
frame.config(bg="blue",width=400,height=300)
frame.pack()

raiz.mainloop()