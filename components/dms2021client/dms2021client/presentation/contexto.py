
from dms2021client.data.rest import AuthService




class Contexto(auth_service: AuthService):
    estado : MenuAbstracto = MenuPrincipal()
    
    def cambiaEstado(menu: MenuAbstracto) : 
        this.estado = menu
    
    def start(): 
        while True:
            this.estado.imprimirEncabezado()
            this.estado.imprimirOpciones()
            this.estado.pedirOpcion()
            this.update()


    def update():
        this.estado.update(this)
                 


