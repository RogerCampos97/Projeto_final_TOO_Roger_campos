from abc import ABC, abstractmethod
from .midia import Midia
from .midia import Midia

class Criador_Midia(ABC):
    def __init__(self, titulo) -> None:
        self.titulo = titulo
    #factory method, responsavel pela criação de cada midia
   
    @abstractmethod
    def factory_midia(self, titulo) -> Midia:
        """
        O método factory abstrato. Cada tipo de midia tem uma classe concreta 
        que é responsável pela criação de cada tipo de midia.
        feito de acordo com o factory method do site refactoring guru
        """
        pass

    def nova_midia(self, titulo: str):
        '''
        aqui logica que define qual tipo de midia vai ser criada

        Args: titulo

        Returns: objeto do tipo midia
        '''

        midia = self.factory_midia(titulo)

        return midia
