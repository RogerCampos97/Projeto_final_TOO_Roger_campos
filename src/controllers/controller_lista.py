import os
import sys
from typing import List
# Adiciona a pasta raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models.midia import Midia

class Lista_Conteudo:
    '''
    lista de mídias que podem ser criadas pelo usuario

        Args: nome da lista
    '''
    def __init__(self, nome: str):
        self.nome = nome
        self._midia: List [Midia] = [] #listas de midia
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, add_nome):
        if not isinstance(add_nome, str):
            raise TypeError("O nome deve ser texto!")
        add_nome = " ".join(add_nome.split())
        if not add_nome:
            raise ValueError("O nome não pode ser vazio!")
        self._nome = add_nome 
        # usar sempre _nome antes do setter pq se não causa loop infinito, 
        # setter chama ele mesmo e não atribui valor

    def add_midia(self, midia_adicionar):
        '''
        fução para adicionar a midia na lista

            Args: objeto do tipo mídia
        '''
        """ if not isinstance(midia, Midia):
            raise TypeError("Falha ao adicionar Item, objeto de tipo inválido")
        if midia in self._midia:
            raise ValueError(f"Falha ao adicionar Item, item Já na lista") """
        self._midia.append(midia_adicionar)
        return midia_adicionar

    def remove_midia(self, midia_dl: Midia):
        if not isinstance(midia_dl, Midia):
            raise TypeError("Tipo inválido")
        if midia_dl in self._midia:
            self._midia.remove(midia_dl)
            return(f"midia removida da coleção {self._nome}!")
        else:
            return(f"midia não encontrada na coleção {self._nome}")

    def listar_conteudo(self):
        '''função para mostrar as midias da lista_conteudo'''
        msg = f"{'='*30}\nMídias na coleção {self._nome}:\n"
        if len(self._midia) == 0:
            msg += "\nNenhuma midia encontrada\n"
        else:
            for i, md in enumerate(self._midia, 1):
                msg += f"{i} - {md}\n"
        msg += f"{'='*30}"
        return msg
    
    """ def mover_midia(self):
        pass

    def selecionar_tipo(self):
        pass """

    def __eq__(self, outro:object):
        if not isinstance(outro, Lista_Conteudo):
                return False
        return (self._nome == outro._nome)
    
    def get_info(self):
        return (f"{self._nome} - [{len(self._midia)}]")
    
    def __str__(self) -> str:
        return (f"{self._nome}")
    
    def __getitem__(self, index):
        return self._midia[index]