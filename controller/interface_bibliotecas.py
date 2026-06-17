import os
import sys
from abc import ABC, abstractmethod
# Adiciona a pasta raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.biblioteca.gerenciar_biblioteca import Gerenciador_biblioteca

class interface:
    def __init__(self) -> None:
        self.gerente = Gerenciador_biblioteca()

class categorias(interface):

    def listar(self):
        print(self.gerente.listar_categorias())
    
    def criar_nova(self):
        try:
            nova_categoria = input("Digite o nome da nova categoria: ")
            print(self.gerente.criar_categoria(nova_categoria))
        except Exception as e:
            print(e)
        else:
            print("certo")

    def add_midia(self):
        pass

class midias(interface):
    def listar_todas(self):
        pass
    def mover_midia(self):
        pass
    
    