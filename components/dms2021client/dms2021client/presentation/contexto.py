from dms2021client.data.rest import AuthService


class Contexto():
    
    def __init__(self, auth_service: AuthService, menu, menuretorno):
        self.estado = menu
        self.auth_service = auth_service
        self.session_id = ""
        self.menuretorno = menuretorno


    def cambiaEstado(self, menu): #tipar la entrada de menú
        self.estado = menu
        self.start()
    
    def start(self):
        self.estado.start(self)
        '''while True:
            self.estado.imprimirEncabezado()
            self.estado.imprimirOpciones()
            self.estado.pedirOpcion()
            self.update()'''


    def update(self):
        self.estado.update(self)

    def get_auth_service(self):
        return self.auth_service
    
                 
    def get_session_id(self):
        return self.session_id

    def set_session_id(self, sessionid):
        self.session_id = sessionid
    
    def retorno(self):
        self.cambiaEstado(self.menuretorno)
    



