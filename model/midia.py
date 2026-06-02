from abc import ABC, abstractmethod
from model.Estado_midia import Estado_Contexto
from datetime import datetime, timedelta

class Midia(ABC):
    def __init__(self, titulo: str):
        self.titulo = titulo
        self.estado_atual = Estado_Contexto()
        self.data_inclusao: datetime
        self.data_atualizado: datetime
        #self.generos: list[Genero] = []
        #self.plataforma_acesso = list[Plataformas]
        self._comentario = None
    
    @property
    def titulo(self):
        return self._titulo
    """ @property
    def tipo(self):
        return self._tipo """
    @property
    def comentario(self):
        return self._comentario
    
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
    
class filmes(Midia):
    def __init__(self, titulo: str):
        super().__init__(titulo)
class livros(Midia):
    def __init__(self, titulo: str):
        super().__init__(titulo)
class Mangas(Midia):
    def __init__(self, titulo: str):
        super().__init__(titulo)
class Animes(Midia):
    def __init__(self, titulo: str):
        super().__init__(titulo)
class Seriados(Midia):
    def __init__(self, titulo: str):
        super().__init__(titulo)
class Jogos(Midia):
    def __init__(self, titulo: str):
        super().__init__(titulo)