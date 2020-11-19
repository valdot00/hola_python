# docstrings = cadenas para documentacion 

def saludar(nombre):
    """
    esto sera un comentario de la fucion saludar.
    esta funcion recibira como parametro unacadena con el nombre e
    imprimira por pantalla un saludo con el nombre concatenado
    """
    print("buenos dias "+nombre)

saludar("antonio")

help(saludar)

class saludos:
    """
    esta clase tendra dos funciones buenos_dias y adios
    ambas fuciones reciviran como parametro un nombre
    """
    def buenos_dias(self,nombre):
        """ esta funcion sirve para decir buenos dias a una persona """
        print("buenos dias {}".format(nombre))

    def adios(self,nombre):
        """esta fucion dice adios a una persona"""
        print("adios {}".format(nombre))    

saludo = saludos()
saludo.buenos_dias("antonio")

help(saludos)