import os
import sys
# Adiciona a pasta raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#from src.views.menu import Menu, MenuItem
from controllers.controller_categorias import controller_categorias

def view_criar_lista_conteudo(controlador: controller_categorias):
        try:
            nova_categoria = input("Digite o nome da nova categoria: ")
            print(controlador.criar_categoria(nova_categoria))
        except Exception as e:
            print(e)
        else:
            print("Categoria criada com sucesso!!!")

def view_listar_listas_conteudo(controlador: controller_categorias):
     print(controlador.listar_categorias())

def view_midias_buscar_midia_global(controlador: controller_categorias, nome: str):
    print("chegou")
    print(controlador.buscar_midia_global(nome))
