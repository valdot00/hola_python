import tkinter

raiz = tkinter.Tk()
raiz.title("radiobutton")

#creamos los radiobutton

def seleccionar():
    print("la opcion selecionada es {}".format(opcion.get()))

opcion = tkinter.IntVar()    

button1 = tkinter.Radiobutton(raiz,text="Opcion 1",variable=opcion, value=1, command=seleccionar)
button1.pack()

button2 = tkinter.Radiobutton(raiz,text="Opcion 2",variable=opcion, value=2, command=seleccionar)
button2.pack()

button3 = tkinter.Radiobutton(raiz,text="Opcion 3",variable=opcion, value=3, command=seleccionar)
button3.pack()

raiz.mainloop()