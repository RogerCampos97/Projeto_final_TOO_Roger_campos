from abc import ABC, abstractmethod
from .estado_midia import Estado_Contexto
from .info_datas import Info_data

class Midia(ABC):
    '''
    Classe abstrata de midia
    '''
    def __init__(self, titulo: str):
        self.titulo = titulo
        self._autor: str | None = None
        self.estado = Estado_Contexto()
        self._datas = Info_data()
        #self.generos: list[Genero] = []
        self._comentario: str | None = None
    
    @property
    def titulo(self):
        return self._titulo
    @property
    def comentario(self):
        return self._comentario
    @property
    def autor(self):
        return self._autor
    
    @titulo.setter
    def titulo(self, add_titulo):
        if not isinstance(add_titulo, str):
            raise TypeError("O nome deve ser texto!")
        add_titulo = " ".join(add_titulo.split())
        if not add_titulo:
            raise ValueError("O nome não pode ser vazio!")
        self._titulo = add_titulo

    @comentario.setter
    def comentario(self, add_comment):
        if not isinstance(add_comment, str):
            raise TypeError("O nome deve ser texto!")
        add_comment = " ".join(add_comment.split())
        if not add_comment:
            raise ValueError("O nome não pode ser vazio!")
        self.titulo = add_comment


    @abstractmethod
    def __eq__(self, outro:object) -> bool:
        pass
    @abstractmethod
    def get_nome(self) ->str:
        pass

    def __str__(self):
        return (f"tipo: {self.__class__.__name__}, nome: {self.titulo}")
    
    def __repr__(self) -> str:
        msg = str(self.__dict__)
        return msg
    
    
    @classmethod
    def obter_tipo_midia(cls) -> list:
        return [sub.__name__ for sub in cls.__subclasses__()]




