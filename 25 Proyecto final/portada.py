from tkinter import *

import operaciones

#funciones para los botones

def comando_visualizar():
    lista.delete(0,END)
    lista_libros = operaciones.Visualizar()
    for libro in lista_libros:
        lista.insert(END,libro)

def comando_buscar():
    lista.delete(0,END)
    lista_libros = operaciones.buscar(titulo.get(),autor.get(),year.get(),isbn.get())
    for libro in lista_libros:
        lista.insert(END,libro)    

def comando_insertar():
    operaciones.insertar(titulo.get(),autor.get(),year.get(),isbn.get())
    lista.delete(0,END)
    lista.insert(END,(titulo.get(),autor.get(),year.get(),isbn.get()))


#creamos la ventana 

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

#lista y scrollbar

lista = Listbox(ventana,height=8,width=25)
lista.grid(row=2,column=0,rowspan=6,columnspan=2)

scrollbar = Scrollbar(ventana)
scrollbar.grid(row=2,column=2,rowspan=6)

lista.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=lista.yview)

#botones

boton1 = Button(ventana,text="Visualizar",width=12,command=comando_visualizar)
boton1.grid(row=2,column=3)

boton2 = Button(ventana,text="Buscar",width=12,command=comando_buscar)
boton2.grid(row=3,column=3)

boton3 = Button(ventana,text="Añadir",width=12,command=comando_insertar)
boton3.grid(row=4,column=3)

boton4 = Button(ventana,text="Actualizar",width=12)
boton4.grid(row=5,column=3)

boton5 = Button(ventana,text="Borrar",width=12)
boton5.grid(row=6,column=3)

boton6 = Button(ventana,text="Cerrar",width=12)
boton6.grid(row=7,column=3)

#titulo
ventana.title("Libros")
ventana.mainloop()