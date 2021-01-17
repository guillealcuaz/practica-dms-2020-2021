from getpass import getpass
from dms2021client.presentation.contexto import Contexto
from dms2021client.presentation.menuabstracto import MenuAbstracto


class MostrarRegistros(MenuAbstracto):

    def __init__ (self):
        self.opcion = 0

    @staticmethod
    def imprimirEncabezado ():
        print("Mostrar Registros \n")

    @staticmethod
    def imprimirOpciones():
        """
        docstring
        """
        #lo que veamos
        print("1.Crear usuario\n"
            "2.Manejar permisos usuario\n"
            "3.Cambiar las reglas del sensor\n"
            "4.Mostrar últimos valores monitorizados\n"
            "5.Cerrar sesión\n")

    def pedirOpcion(self):
        """
        docstring
        """
        self.opcion = int(input("Introduzca el número de la opción elegida: "))

    def update(self,contexto: Contexto):
        """
        docstring
        """
        contexto.retorno()
