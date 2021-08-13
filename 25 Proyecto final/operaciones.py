import sqlite3
from sqlite3.dbapi2 import Cursor

def conectar():
    conexion = sqlite3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS libros(id INTEGER PRIMARY KEY, titulo TEXT, autor TEXT, year INTEGER, isbn INTEGER)")
    conexion.commit()
    conexion.close()

def insertar(titulo,autor,year,isbn):
    conexion = sqlite3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO libros VALUES (NULL,?,?,?,?)",(titulo,autor,year,isbn)) 
    conexion.commit()
    conexion.close()   

def Visualizar():
    conexion = sqlite3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM libros")
    resultado = cursor.fetchall()
    conexion.close()
    return resultado  

def buscar(titulo='',autor='',year=0,isbn=0):
    conexion = sqlite3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM libros WHERE titulo=? OR autor=? OR year=? OR isbn=?",(titulo,autor,year,isbn))
    resultado = cursor.fetchall()
    conexion.close()
    return resultado

def borrar(id):
    conexion = sqlite3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM libros WHERE id=?",(id,))
    conexion.commit()
    conexion.close()

def Actualizar(titulo,autor,year,isbn,id):
    conexion = sqlite3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute("UPDATE libros SET titulo=?, autor=?, year=?, isbn=? WHERE id=?",(titulo,autor,year,isbn,id))
    conexion.commit()
    conexion.close()
    
#pruebas
conectar()

#test insertar
#insertar("titulo1","autor1",2001,123456789)
#insertar("titulo2","autor2",2002,123456789)
#insertar("titulo3","autor3",2003,123456789)

#resultados = Visualizar()
#for resultado in resultados:
#    print(resultado)

#resultados = buscar(titulo='titulo1')
#resultados = Visualizar()
#for resultado in resultados:
#    print(resultado)

#test borrar
#borrar(2)
#resultados = Visualizar()
#for resultado in resultados:
#    print(resultado)

#test actualizar
Actualizar(titulo="titulo3",autor="autor3",year=2003,isbn=987654321,id=1)
resultados = Visualizar()

for resultado in resultados:
    print(resultado)
