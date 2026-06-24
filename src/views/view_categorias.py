import os
import sys
# Adiciona a pasta raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

#from src.views.menu import Menu, MenuItem
from src.controllers.controller_categorias import controller_categorias

def criar_lista_conteudo(controlador: controller_categorias):
        try:
            nova_categoria = input("Digite o nome da nova categoria: ")
            print(controlador.criar_categoria(nova_categoria))
        except Exception as e:
            print(e)
        else:
            print("Categoria criada com sucesso!!!")

def listar_categorias(controlador: controller_categorias):
    try:
        print(controlador.listar_categorias())
    except Exception as e:
        print(e)

def buscar_midia_global(controlador: controller_categorias):
    try:
        nome = input("Digite o nome da midia para buscar: ")
        print(controlador.buscar_midia_global(nome))
    except Exception as e:
        print(e)