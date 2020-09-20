# 77 borrar datos 

import sqlite3

conexion = sqlite3.connect("basededatos1.db")

cursor = conexion.cursor()

cursor.execute("DELETE FROM PERSONAS WHERE nombre = 'luis'")

conexion.commit()
conexion.close()