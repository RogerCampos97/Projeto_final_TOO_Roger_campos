import os
import sys
from typing import List
# Adiciona a pasta raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from .controller_lista import Lista_Conteudo
from src.models.midia import Midia
from src.models.factory_midia import Factory_Midia

class SingletonMeta(type): 
    '''
    implementação do padrao singleton para garantir que apenas 
    um gerenciador de biblioteca exista, mesmo que outro seja 
    instanciado ele será o mesmo gerenciador.
    '''
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
    
    def _clear_instance(cls):
        if cls in cls._instances:
            del cls._instances[cls]

class controller_categorias(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self._lista_midias: List [Midia] = [] # lista com todas as midias
        self._bibliotecas: List [Lista_Conteudo] = []# listas com listas de midia

    def criar_categoria(self, nome: str):
        '''
        criar novo objeto tipo lista_conteudo e faz
        o append na lista do gerenciador

            Args: 
                nome = nome da lista str
        '''
        entrada = Lista_Conteudo(nome)
        if entrada not in self._bibliotecas:
            self._bibliotecas.append(entrada)
            return ("Nova categoria da biblioteca criada!")
        else:
            raise ValueError(f"Já existe Categoria com o nome [{entrada}], tente outro nome!") 

    def excluir_categoria(self, biblioteca: Lista_Conteudo) -> bool:
        '''
        excluir uma lista da tipo lista_conteudo da lista bibliotecas 

            Args: 
                biblioteca = lista_conteudo
            Returns: 
                true or false
        '''
        try:
            self._bibliotecas.remove(biblioteca)
            return True
        except ValueError:
            return False  # não encontrado

    def buscar_midia_global(self, nome: str):
        '''
        buscar uma midia na lista global de todas as midias disponiveis
            Args: 
                nome = nome da midia
            Returns: 
                objeto do tipo midia ou None
        '''
        for m in self._lista_midias:
            if m.titulo == nome:
                return m
        return None
    
    def listar_categorias(self):
        '''fução para mostrar as listas de midia'''

        msg = f"{'='*30}\nColeçóes:\n1 - Padrão[{len(self._lista_midias)}]\n"
        for i, mdlista in enumerate(self._bibliotecas, 2):
            msg += f"{i} - {mdlista.get_info()}\n"
        msg += f"{'='*30}"
        return msg

    def retornar_categoria(self, index: int) -> Lista_Conteudo:
        '''
        recebe um indice e retorna uma categoria
        '''
        selected = None

        if 0 <= index < len(self._bibliotecas):
            selected = self._bibliotecas[index]
        if selected:
            return selected
        else:
            raise IndexError("Indice inválido para categoria")
    

    def listar_lista_global(self):
        '''fução para mostrar as midias da lista_global'''
        msg = f"{'='*30}\nMídias na coleção Padrão:\n"
        if len(self._lista_midias) == 0:
            msg += "\nNenhuma midia encontrada\n"
        else:
            for i, md in enumerate(self._lista_midias, 1):
                msg += f"{i} - {md}\n"
        msg += f"{'='*30}"
        return msg
     
    def append_midia(self,md: Midia, index: int | None = None ):
        if not isinstance(md, Midia):
            print("rodou no teste")
            raise TypeError("Falha ao adicionar Item, objeto de tipo inválido")
        if md in self._lista_midias:
            raise ValueError(f"Falha ao adicionar Item, item Já na lista")
        self._lista_midias.append(md)
        msg = ("Midia adicionada a coleção Padrão\n")

        if index is not None:
            add_midia = self._bibliotecas[index].add_midia(md)
            msg +=(f"Midia adicionada a coleção {self._bibliotecas[index]}") if add_midia else ""
        return msg