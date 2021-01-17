from getpass import getpass
from dms2021client.presentation.contexto import Contexto
from dms2021client.presentation.menuabstracto import MenuAbstracto
from dms2021core.data.userrightname import UserRightName


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
        print("Lista con las últimas 5 entradas del sensor elegido.")

    def pedirOpcion(self):
        """
        docstring
        """
        self.opcion = int(input("Introduzca el número del sensor elegido: "))

    def update(self,contexto: Contexto):
        """
        docstring
        """
        try:
            if contexto.get_auth_service().has_right(contexto.get_username(), UserRightName(4).name):
                sensores = [contexto.get_sensor1_service(), contexto.get_sensor2_service()]
                sensores[self.opcion-1].latest_entries()
            contexto.retorno()
        except IndexError:
            print("\nLa opción seleccionada no existe\n",
            "Volviendo al menu principal\n")
            contexto.retorno()
