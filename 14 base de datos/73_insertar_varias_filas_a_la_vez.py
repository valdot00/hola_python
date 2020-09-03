#73 insertar varias filas a la vez

import sqlite3

conexion = sqlite3.connect("basededatos1.db")

cursor = conexion.cursor()

lista_personas = [('pedro','rodigez','perez',26), ('maria','lopez','gomez',46), ('jorge','pelayo','arellano',28)]

cursor.executemany("INSERT INTO PERSONAS VALUES (?,?,?,?)", lista_personas)

conexion.commit()

conexion.close()