#ejercicio

#crear una base de datos "basededatos2.db"
#crear una tabla "productos" con 3 campos
       #id: identificador del procuto de tipo numerico
       #nombre: nombre del producto de tipo texto
       #precio: precio del producto de tipo numerico

#insertar 3 ´productos en la tabla "productos"
# 1,"impresora",300
# 2,"raton",20
# 3,"ordenador",600

#consultar los productos de la tabla "productos"
# cerrar la base de datos "basededatos.db"

import sqlite3

conexion = sqlite3.connect("basededatos2.db")

cursor = conexion.cursor()
cursor.execute("CREATE TABLE PRODUCTOS (ID INTEGER, NOMBRE TEXT, PRECIO INTEGER)")

conexion.commit()

cursor.execute("INSERT INTO PRODUCTOS VALUES (1,'IMPRESORA',300)")
conexion.commit()

cursor.execute("INSERT INTO PRODUCTOS VALUES (2,'RATON',20)")
conexion.commit()

cursor.execute("INSERT INTO PRODUCTOS VALUES (1,'OREDENADOR',600)")
conexion.commit()

cursor.execute("SELECT * FROM PRODUCTOS")
productos = cursor.fetchall()
for producto in productos:
    print(producto)

conexion.close()