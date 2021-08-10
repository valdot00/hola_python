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

#entrada de datos

titulo = StringVar()
entrada1 = Entry(ventana,textvariable=titulo)
entrada1.grid(row=0,column=1)

autor = StringVar()
entrada2 = Entry(ventana,textvariable=autor)
entrada2.grid(row=0,column=3)

year = StringVar()
entrada3 = Entry(ventana,textvariable=year)
entrada3.grid(row=1,column=1)

isbn = StringVar()
entrada4 = Entry(ventana,textvariable=isbn)
entrada4.grid(row=1,column=3)

#titulo
ventana.title("Libros")
ventana.mainloop()

