import tkinter

raiz = tkinter.Tk()
raiz.title("radiobutton")

# creamos los radiobutton

def seleccionar():
    print("la opcion seleccionada es {}".format(opcion.get()))

opcion = tkinter.IntVar()

botonradio1 = tkinter.Radiobutton(raiz,text="opcion 1",variable=opcion,value=1,command=seleccionar)
botonradio1.pack()

raiz.mainloop()