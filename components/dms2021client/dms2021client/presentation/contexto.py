from dms2021client.data.rest import AuthService


class Contexto():

    auth_service : AuthService = None
    
    def __init__(self, auth_service: AuthService, menu):
        self.estado = menu
        self.auth_service = auth_service

    def cambiaEstado(self, menu): #tipar la entrada de menú
        self.estado = menu
    
    def start(self):
        while True:
            self.estado.imprimirEncabezado()
            self.estado.imprimirOpciones()
            self.estado.pedirOpcion()
            self.update()


    def update(self):
        self.estado.update(self)
                 


