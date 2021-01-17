from getpass import getpass
from dms2021client.presentation.contexto import Contexto
from dms2021client.presentation.menuabstracto import MenuAbstracto
from dms2021client.presentation.menuautenticacion import MenuAutenticacion
from dms2021client.presentation.menucrearusuario import MenuCrearUsuario


class ModificarReglas (MenuAbstracto):
    
    def __init__ (self):
        self.route = "/"
        self.time = 1000000

    @staticmethod
    def imprimirEncabezado ():
        print("Modificar Reglas \n")
    
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
        self.route = input("Introduzca la ruta elegida: ")
        self.time = int(input("Introduzca el periodo de monitorización elegido en ms: "))

    
    def update(self,contexto: Contexto):
        """
        docstring
        """ 
        contexto.retorno()
    
        

