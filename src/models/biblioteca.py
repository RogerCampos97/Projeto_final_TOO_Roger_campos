from .midia import Midia
from typing import List

class Lista_Conteudo:
    '''
    lista de mídias que podem ser criadas pelo usuario

        Args: nome da lista
    '''
    def __init__(self, nome: str):
        self.nome = nome
        self._midia: List[Midia] = []
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, add_nome):
        print("chegou no setter")
        if not isinstance(add_nome, str):
            raise TypeError("O nome deve ser texto!")
        add_nome = " ".join(add_nome.split())
        if not add_nome:
            raise ValueError("O nome não pode ser vazio!")
        self._nome = add_nome 
        # usar sempre _nome antes do setter pq se não causa loop infinito, 
        # setter chama ele mesmo e não atribui valor

    def add_midia(self, midia):
        '''
        fução para adicionar a midia na lista

            Args: objeto do tipo mídia
        '''
        if not isinstance(midia, Midia):
            raise TypeError("Falha ao adicionar Item, objeto de tipo inválido")
        if midia in self._midia:
            return(f"Falha ao adicionar Item, item Já no inventário")
        self._midia.append(midia)
        return(f"Midia adicionada a coleção {self._nome}")

    def remove_midia(self, midia):
        '''
        fução para remover a midia na lista

            Args: objeto do tipo mídia
        '''
        if midia in self._midia:
            self._midia.remove(midia)
            return(f"midia removida da coleção {self._nome}!")
        else:
            return(f"midia não encontrada na coleção {self._nome}")
        
    def listar_conteudo(self):
        '''fução para mostrar as midias da lista_conteudo'''
        msg = f"\nMídias na coleção {self._nome}:\n"
        for i, md in enumerate(self._midia, 1):
            msg += f"{i} - {md}\n"
        return msg
    
    def __eq__(self, outro:object):
        if not isinstance(outro, Lista_Conteudo):
                return False
        return (self._nome == outro._nome)
    
    def get_info(self):
        return (f"{self._nome} - [{len(self._midia)}]")
    
    def __str__(self) -> str:
        return (f"{self._nome}")