from getpass import getpass
from dms2021client.presentation.contexto import Contexto
from dms2021client.presentation.menuabstracto import MenuAbstracto
from dms2021client.presentation.menuautenticacion import MenuAutenticacion
from dms2021client.presentation.menucrearusuario import MenuCrearUsuario
from dms2021core.data.userrightname import UserRightName


class ModificarReglas (MenuAbstracto):
    
    def __init__ (self):
        self.route = "/"
        self.time = 1000000
        self.sensor = 1

    @staticmethod
    def imprimirEncabezado ():
        print("Modificar Reglas \n")
    
    @staticmethod
    def imprimirOpciones():
        """
        docstring
        """
        print("Aqui puede determinar la frecuencia de la monitorización\n"
        "y la ruta que se comprueba")


    def pedirOpcion(self):
        """
        docstring
        """
        self.route = input("Introduzca la ruta elegida: ")
        self.time = int(input("Introduzca el periodo de monitorización elegido en ms: "))
        self.sensor = int(input("Introduzca el número de sensor elegido"))


    def update(self,contexto: Contexto):
        """
        docstring
        """
        try:
            if contexto.get_auth_service().has_right(contexto.get_username(), UserRightName(4).name):
                sensores = [contexto.get_sensor1_service(), contexto.get_sensor2_service()]
                sensores[self.sensor-1].modify_rules(self.time, self.route)
            contexto.retorno()
        except IndexError:
            print("\nLa opción seleccionada no existe\n",
            "Volviendo al menu principal\n")
            contexto.retorno()