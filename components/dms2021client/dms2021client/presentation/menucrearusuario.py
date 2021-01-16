from getpass import getpass
from dms2021client.presentation.contexto import Contexto
from dms2021client.presentation.menuabstracto import MenuAbstracto
from dms2021client.presentation.menuprincipal import MenuPrincipal

class MenuCrearUsuario(MenuAbstracto):

    def __init__ (self):
        self.usuario = ""
        self.contrasena = ""

    @staticmethod
    def imprimirEncabezado ():
        print(":Menu Crear Usuario: \n")
    
    @staticmethod
    def imprimirOpciones():
        """
        docstring
        """
        print("Crear usuario nuevo: ")

    
    def pedirOpcion(self):
        """
        docstring
        """
        self.usuario = input("Introduzca usuario nuevo: ")
        self.contrasena = getpass("Introduzca nueva contrasena: ")
        
    def update(self, contexto: Contexto):
        """
        docstring
        """
        sesion = contexto.get_session_id()
        contexto.get_auth_service().create_user(self.usuario, self.contrasena, sesion)
        respuesta = input("¿Quiere crear otro usuario? (S/N)\n")
        if respuesta == "s" or respuesta == "S":
            contexto.cambiaEstado(MenuCrearUsuario()) 
        else:
            contexto.cambiaEstado(MenuPrincipal())
        
    
