from abc import ABC, abstractmethod
from .midia import Midia

class factory_Midia(ABC):#factory method, responsavel pela criação de cada midia
    def __init__(self, titulo) -> None:
        self.titulo = titulo
   
    @abstractmethod
    def factory_midia(self, titulo) -> Midia:
        """
        O método factory abstrato. Cada tipo de midia tem uma classe concreta 
        que é responsável pela criação de cada tipo de midia.
        feito de acordo com o factory method do site refactoring guru
            Args: titulo
            Returns: objeto do tipo midia
        """
        pass
