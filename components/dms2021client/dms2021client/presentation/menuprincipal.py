from getpass import getpass
from dms2021client.presentation.contexto import Contexto
from dms2021client.presentation.menuabstracto import MenuAbstracto
from dms2021client.presentation.menuautenticacion import MenuAutenticacion
from dms2021client.presentation.menucrearusuario import MenuCrearUsuario


class MenuPrincipal (MenuAbstracto):
    
    def __init__ (self):
        self.opcion = 0
        

    @staticmethod
    def imprimirEncabezado ():
        print(":Menu Principal \n")
    
    @staticmethod
    def imprimirOpciones():
        """
        docstring
        """
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
        
        menus = [MenuCrearUsuario(),0,0,0,MenuAutenticacion()]
        
        try:
            if self.opcion == 5:
                sesion = contexto.get_session_id()
                contexto.get_auth_service().logout(sesion)
            
            contexto.cambiaEstado(menus[self.opcion-1])
        except IndexError:
            print("\nLa opción seleccionada no existe\n",
            "Volviendo al menu principal\n")
            contexto.cambiaEstado(MenuPrincipal())
        

