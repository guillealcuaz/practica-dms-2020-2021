from dms2021client.presentation.contexto import Contexto
from dms2021client.presentation.menuabstracto import MenuAbstracto
from dms2021client.presentation.concederpermisos import ConcederPermisos
from dms2021client.presentation.revocarpermisos import RevocarPermisos

class GestionPermisosUsuario(MenuAbstracto):

    def __init__ (self):
        self.opcion = 0
        self.usuario = ""

    @staticmethod
    def imprimirEncabezado ():
        print("Gestion de permisos de usuario \n")
    
    @staticmethod
    def imprimirOpciones():
        """
        docstring
        """
        print("1.Conceder permiso\n"
            "2.Revocar permiso\n"
            "3.Menu principal")

    
    def pedirOpcion(self):
        """
        docstring
        """
        self.opcion = int(input("Introduzca el número de la opción elegida: "))

    
    def update(self,contexto: Contexto):
        """
        docstring
        """
        
        menus = [ConcederPermisos(), RevocarPermisos()]
        
        try:
            if self.opcion == 3:
                contexto.retorno()         
            contexto.cambiaEstado(menus[self.opcion-1])
        except IndexError:
            print("\nLa opción seleccionada no existe\n",
            "Volviendo al menu principal\n")
            contexto.retorno()


