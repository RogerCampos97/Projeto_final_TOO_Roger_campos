from abc import ABC, abstractmethod
from model.midia.midia import Midia

class Biblioteca:
    def __init__(self, nome: str):
        self.nome = nome
        self._midia = []
    
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

    def add_midia(self, midia):
        if not isinstance(midia, Midia):
            raise TypeError("Falha ao adicionar Item, objeto de tipo inválido")
        if midia in self._midia:
            return(f"Falha ao adicionar Item, item Já no inventário")
        self._midia.append(midia)
        return(f"Midia adicionada a coleção {self.nome}")

    def remove_midia(self, midia):
        if midia in self._midia:
            self._midia.remove(midia)
            return(f"midia removida da coleção!")
        else:
            return(f"midia não encontrada")
        
    def listar_conteudo(self):
        msg = f"\nMídias na coleção {self.nome}:\n"
        for i, md in enumerate(self._midia, 1):
            msg += f"{i} - {md}\n"
        return msg
    