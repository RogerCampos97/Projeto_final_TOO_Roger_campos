import os
import sys
from typing import List
# Adiciona a pasta raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controllers.controller_lista import Lista_Conteudo
from models.midia import Midia

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

class controller_categorias(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self._lista_midias: List [Midia] = [] # lista com todas as midias
        self._bibliotecas: List [Lista_Conteudo] = []# listas com listas de midia

    def criar_categoria(self, nome: str):
        '''
        criar novo objeto tipo lista_conteudo e faz
        o append na lista do gerenciador

            Args: 
                nome = nome da lista
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
        print("chegou aqui")
        msg = "\nColeçóes:\n"
        for i, mdlista in enumerate(self._bibliotecas, 1):
            msg += f"{i} - {mdlista.get_info()}\n"
        return msg

