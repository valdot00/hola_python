# pydoc - generar documentacion automatica desde
# la consola o terminal de comandos

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

