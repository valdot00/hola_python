from tkinter import *

ventana = Tk() 

#CREAMOS LAS ETIQUETAS

etiqueta1 = Label(ventana,text="titulo")
etiqueta1.grid(row=0,column=0)

etiqueta2 = Label(ventana,text="Autor")
etiqueta2.grid(row=0,column=2)

etiqueta3 = Label(ventana,text="Año")
etiqueta3.grid(row=1,column=0)

etiqueta4 = Label(ventana, text="ISBN")
etiqueta4.grid(row=1,column=2)

ventana.title("Libros")
ventana.mainloop()

