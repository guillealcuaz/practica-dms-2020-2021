from abc import ABC,abstractmethod
from dms2021client.presentation.contexto import Contexto
class MenuAbstracto (ABC): 

    @abstractmethod 
    def imprimirEncabezado(self):
        """
        docstring
        """
        print("Encabezado por defecto")
    
    @abstractmethod 
    def imprimirOpciones(self):
        """
        docstring
        """
        print("1: Opcion 1:\n 2: Opcion 2:  ")

    @abstractmethod 
    def pedirOpcion(self):
        """
        docstring
        """
        print("Introduzca la opcion deseada en forma numerica\n")

    @abstractmethod 
    def update(self, contexto: Contexto):
        """
        docstring
        """
        pass
