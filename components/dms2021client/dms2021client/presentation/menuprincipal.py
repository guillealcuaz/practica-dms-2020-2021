from getpass import getpass
from dms2021client.presentation.contexto import Contexto
from dms2021client.presentation.menuabstracto import MenuAbstracto

class MenuPrincipal (MenuAbstracto):
    opcion = 0
    @staticmethod
    def imprimirEncabezado ():
        print(":Menu Principal prueba\n")
    
    @staticmethod
    def imprimirOpciones():
        """
        docstring
        """
        print("1: Opcion 1:\n 2: Opcion 2:  ")

    @staticmethod
    def pedirOpcion():
        """
        docstring
        """
        print(getpass("Di una palabra: "))

    @staticmethod
    def update(contexto: Contexto):
        """
        docstring
        """
        contexto.cambiaEstado(MenuPrincipal())
