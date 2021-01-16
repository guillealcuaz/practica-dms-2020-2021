from dms2021client.presentation.contexto import Contexto
from dms2021client.presentation.menuabstracto import MenuAbstracto
from dms2021core.data import UserRightName

class RevocarPermisos(MenuAbstracto):

    def __init__ (self):
        self.opcion = 0
        self.usuario = ""

    @staticmethod
    def imprimirEncabezado ():
        print("Revocar permisos de usuario \n")
    
    @staticmethod
    def imprimirOpciones():
        """
        docstring
        """
        print("Lista de permisos:\n"
            "1.Admin usuarios\n"
            "2.Admin permisos\n"
            "3.Admin sensores (no se usa)\n"
            "4.Admin reglas\n"
            "5.Ver informes\n")

    
    def pedirOpcion(self):
        """
        docstring
        """
        self.opcion = int(input("Introduzca el número del permiso elegido: "))
        self.usuario = input("Introduzca el nombre del usuario elegido: ")

    
    def update(self,contexto: Contexto):
        """
        docstring
        """
        sesion = contexto.get_session_id()
        contexto.get_auth_service().revoke(self.usuario, UserRightName(self.opcion).name, sesion)
        respuesta = input("¿Quiere revocar otro permiso? (S/N)\n")
        if respuesta == "s" or respuesta == "S":
            contexto.cambiaEstado(RevocarPermisos()) 
        else:
            contexto.retorno()

