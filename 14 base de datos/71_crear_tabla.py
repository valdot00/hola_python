#71 crear tabla

#SQLite3 -crear una tabla en nuestra base de datos

import sqlite3

conexion = sqlite3.connect("basededatos1.db")

cursor = conexion.cursor() 

cursor.execute("CREATE TABLE PERSONAS (nombre TEXT,apellido TEXT,apellido2 TEXT, edad INTEGER)")

conexion.commit()

conexion.close()
