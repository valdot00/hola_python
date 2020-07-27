# 54 incluir datos en un fichero

fichero = open("fichero_para_grabar.txt","at")

cadena_para_incluir = "\nesta es la tercera fila del fichero"

fichero.write(cadena_para_incluir)

fichero.close()