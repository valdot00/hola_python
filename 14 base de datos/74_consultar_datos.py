#74 consultar datos 

import sqlite3 

conexion = sqlite3.connect("basededatos1.db")

cursor = conexion.cursor()

cursor.execute("SELECT * FROM PERSONAS")

persona = cursor.fetchall()

for persona in persona:
    print(persona)

conexion.close()    