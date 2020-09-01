#72 insertar una fila

#sqlite3 -insertar datos en nuestra tabla

import sqlite3

conexion = sqlite3.connect("basededatos1.db")

cursor = conexion.cursor()

cursor.execute("INSERT INTO PERSONAS VALUES ('Antorio','Perez','Gomez',35)")

conexion.commit()

conexion.close()