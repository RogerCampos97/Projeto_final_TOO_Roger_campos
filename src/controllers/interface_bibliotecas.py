import os
import sys
from abc import ABC, abstractmethod
# Adiciona a pasta raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from src.model.midia.factory_midia import factory_Midia
from view.menu import Menu, MenuItem

class interface(ABC):
    def __init__(self) -> None:
        self.gerente = Gerenciador_biblioteca()
    
    @abstractmethod
    def criar_nova(self):
        pass

class categorias(interface):
    
    def criar_nova(self):
        super().criar_nova()
        try:
            nova_categoria = input("Digite o nome da nova categoria: ")
            print(self.gerente.criar_categoria(nova_categoria))
        except Exception as e:
            print(e)
        else:
            print("Categoria criada com sucesso!!!")

    def listar(self):
        print(self.gerente.listar_categorias())

    def add_midia(self):
        pass

class midias(interface):
    def criar_nova(self):
        super().criar_nova()
        try:
            nome_midia = input("Digite o nome da nova midia a ser criada: ")
            menu_criar = Menu("Tipo de Midia")

            #menu_criar.add_item(MenuItem("Anime", acao=factory_Midia.nova_midia(nome_midia, "anime")))
            tipo = input("Digite o tipo da midia: ")
            
            #self.
            #print(factory_Midia.nova_midia(nova_midia, )
        except Exception as e:
            print(e)
        else:
            print("Nova midia criada com sucesso Concluído")

    def listar_todas(self):
        pass
    def mover_midia(self):
        pass
    def selecionar_tipo(self):
        pass