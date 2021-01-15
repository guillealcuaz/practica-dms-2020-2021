from dms2021client.data.rest import AuthService
from dms2021client.presentation.menuprincipal import MenuPrincipal
from dms2021client.presentation.menuabstracto import MenuAbstracto


class Contexto():

    estado : MenuAbstracto = MenuPrincipal()
    auth_service : AuthService = None
    
    def __init__(self, auth_service: AuthService):
        self.auth_service = auth_service

    def cambiaEstado(self, menu: MenuAbstracto):
        self.estado = menu
    
    def start(self):
        while True:
            self.estado.imprimirEncabezado()
            self.estado.imprimirOpciones()
            self.estado.pedirOpcion()
            self.update()


    def update(self):
        self.estado.update(self)
                 


