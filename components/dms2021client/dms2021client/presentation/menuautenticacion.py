from getpass import getpass
from dms2021client.presentation.contexto import Contexto
from dms2021client.presentation.menuabstracto import MenuAbstracto
from dms2021client.data.rest.exc import InvalidCredentialsError

class MenuAutenticacion(MenuAbstracto):

    def __init__ (self):
        self.usuario = ""
        self.contrasena = ""

    @staticmethod
    def imprimirEncabezado ():
        print(":Menu Autenticacion: \n")
    
    @staticmethod
    def imprimirOpciones():
        """
        docstring
        """
        print("Introduce Usuario y Contraseña: ")

    
    def pedirOpcion(self):
        """
        docstring
        """
        self.usuario = input("Usuario : ")
        self.contrasena = getpass("Contraseña : ")


    def update(self, contexto: Contexto):
        """
        docstring
        """
        
        try:
            sesion = contexto.auth_service.login(self.usuario, self.contrasena)
            contexto.set_session_id(sesion)
            contexto.set_username(self.usuario)
            contexto.retorno()
        except InvalidCredentialsError:
            print("Usuario y/o contraseña incorrecto/s")
            contexto.cambiaEstado(MenuAutenticacion())
        

