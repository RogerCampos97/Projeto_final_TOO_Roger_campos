from abc import ABC, abstractmethod

class Biblioteca(ABC):
    def __init__(self, nome: str):
        self.nome = nome
        self.midia = []
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, add_nome):
        if not isinstance(add_nome, str):
            raise TypeError("O nome deve ser texto!")
        novo_nome = " ".join(add_nome.split())
        if not add_nome:
            raise ValueError("O nome não pode ser vazio!")
        self._nome = add_nome