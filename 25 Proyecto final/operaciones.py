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

#pruebas
conectar()
insertar("titulo1","autor1",2000,123456789)
resultados = Visualizar()
for resultado in resultados:
    print(resultado)


