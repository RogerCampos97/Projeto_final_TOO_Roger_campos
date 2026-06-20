import os
import sys
# Adiciona a pasta raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#from src.views.menu import Menu, MenuItem
from controllers.controller_listas_conteudo import controller_listas

def view_criar_lista_conteudo(controlador: controller_listas):
        try:
            nova_categoria = input("Digite o nome da nova categoria: ")
            print(controlador.criar_categoria(nova_categoria))
        except Exception as e:
            print(e)
        else:
            print("Categoria criada com sucesso!!!")

def view_listar_listas_conteudo(controlador: controller_listas):
     print(controlador.listar_categorias())