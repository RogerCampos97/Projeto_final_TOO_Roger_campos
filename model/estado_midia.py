from abc import ABC, abstractmethod
#from model.midia import Midia

class Estado_midia(ABC):
    def __init__(self, midia):
        self.midia = midia

    @property 
    def midia(self):
        return self.midia
    
    @midia.setter
    def midia(self, atribuir_midia):
        from model.midia import Midia
        if not isinstance(atribuir_midia, Midia):
            raise TypeError("Erro, objeto não é uma missão")
        self.midia = atribuir_midia
    
    @abstractmethod
    def iniciar(self) -> 'Estado_midia':
        pass
    @abstractmethod
    def pausar(self) -> 'Estado_midia':
        pass
    @abstractmethod
    def concluir(self) -> 'Estado_midia':
        pass

    @abstractmethod
    def get_nome(self) -> 'str':
        pass

    def __str__(self):
        return (f"{self.__class__.__name__}")
   
    def __eq__(self, outro:object) -> bool:
        if not isinstance(outro, Estado_midia):
            return False
        return (self.__class__.__name__ == outro.__class__.__name__)
