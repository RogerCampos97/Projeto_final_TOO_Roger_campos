import os
import sys
from abc import ABC, abstractmethod
# Adiciona a pasta raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.biblioteca.gerenciar_biblioteca import Gerenciador_biblioteca


class interface:
    def __init__(self) -> None:
        self.gerente = Gerenciador_biblioteca()



class listas(interface):

    def listar(self):
        print("Todas as categorias:\n")
        print(self.gerente.listar_bibliotecas())
    
    def criar_nova(self):
        pass

    def add_midia(self):
        pass

class midias(interface):
    def listar_todas(self):
        pass
    def mover_midia(self):
        pass
    
    