from abc import ABC, abstractmethod

class Midia(ABC):
    def __init__(self, titulo: str, tipo):
        self.titulo = titulo
        self._tipo = tipo# alterar dps p tipo
        #self.estado_atual = Estado_atual
        #self.data_inclusao: date
        #self.data_atualizado: date
        #self.genero: list[Genero] = []
        #self.plataforma_acesso = list[Plataformas]
        self._comentario = None
    
    @property
    def titulo(self):
        return self.titulo
    @property
    def tipo(self):
        return self._tipo
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
        self.titulo = add_titulo

    @comentario.setter
    def comentario(self, add_comment):
        if not isinstance(add_comment, str):
            raise TypeError("O nome deve ser texto!")
        novo_nome = " ".join(add_comment.split())
        if not add_comment:
            raise ValueError("O nome não pode ser vazio!")
        self.titulo = add_comment

    def __eq__(self, outro:object) -> bool:
        if not isinstance(outro, Midia):
            return False
        return (self.titulo == outro.titulo 
                and self.tipo == outro.tipo)
    
    @abstractmethod
    def __str__(self):
        return (f"{self.titulo}")
    