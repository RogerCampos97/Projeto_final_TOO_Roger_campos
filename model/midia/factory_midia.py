from abc import ABC, abstractmethod
from .base import Midia

class Criador_Midia(ABC):
    def __init__(self, titulo) -> None:
        self.titulo = titulo
    #factory method, responsavel pela criação de cada midia
   
    @abstractmethod
    def criar_midia(self, titulo) -> Midia:
        """
        O método factory abstrato. O tipo de retorno deve corresponder 
        à inteface de cada tipo.
        """
        pass

    @staticmethod
    def nova_midia(titulo: str):
        '''
        aqui logica factory
        '''

        midia = Criador_Midia.criar_midia(titulo)

        return midia
