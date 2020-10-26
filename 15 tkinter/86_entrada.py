import tkinter

raiz = tkinter.Tk()
raiz.title("entrada")

entrada = tkinter.Entry(raiz)
entrada.config(justify="center")
entrada.pack()

raiz.mainloop()