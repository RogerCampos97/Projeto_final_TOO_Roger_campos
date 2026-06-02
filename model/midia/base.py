from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from midia.Estado_midia import Estado_Contexto

class Midia(ABC):
    def __init__(self, titulo: str):
        self.titulo = titulo
        self.estado_atual = Estado_Contexto()
        self._data_inclusao: datetime
        self._data_atualizado: datetime
        #self.generos: list[Genero] = []
        #self.plataforma_acesso = list[Plataformas]
        self._comentario = None
    
    @property
    def titulo(self):
        return self._titulo
    @property
    def comentario(self):
        return self._comentario
    @property
    def data_inclusao(self):
        return self._data_inclusao
    @property
    def data_atualizado(self):
        return self._data_atualizado
    
    @titulo.setter
    def titulo(self, add_titulo):
        if not isinstance(add_titulo, str):
            raise TypeError("O nome deve ser texto!")
        novo_nome = " ".join(add_titulo.split())
        if not add_titulo:
            raise ValueError("O nome não pode ser vazio!")
        self._titulo = add_titulo

    @comentario.setter
    def comentario(self, add_comment):
        if not isinstance(add_comment, str):
            raise TypeError("O nome deve ser texto!")
        novo_nome = " ".join(add_comment.split())
        if not add_comment:
            raise ValueError("O nome não pode ser vazio!")
        self.titulo = add_comment
    
    @data_inclusao.setter
    def data_inclusao(self, add_data):
        if not isinstance(add_data, datetime):
            raise TypeError("Deve ser data!")
        self.data_inclusao = add_data
    
    @data_atualizado.setter
    def data_atualizado(self, add_data):
        if not isinstance(add_data, datetime):
            raise TypeError("Deve ser data!")
        self.data_atualizado = add_data

    @abstractmethod
    def __eq__(self, outro:object) -> bool:
        pass
        '''
        if not isinstance(outro, Midia):
            return False
        return (self.titulo == outro.titulo)
        '''
        
    @abstractmethod
    def __str__(self):
        return (f"{self.titulo}")
    





