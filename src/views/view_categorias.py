import os
import sys
# Adiciona a pasta raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

#from src.views.menu import Menu, MenuItem
from src.controllers.controller_categorias import controller_categorias

def criar_lista_conteudo(ctrl: controller_categorias):
    try:
        nova_categoria = input("Digite o nome da nova categoria: ")
        print(ctrl.criar_categoria(nova_categoria))
    except Exception as e:
        print(e)
    else:
        print("Categoria criada com sucesso!!!")

def listar_categorias(ctrl: controller_categorias):
    try:
        print(ctrl.listar_categorias())
    except Exception as e:
        print(e)

def buscar_midia_global(ctrl: controller_categorias):
    try:
        nome = input("Digite o nome da midia para buscar: ")
        print(ctrl.buscar_midia_global(nome))
    except Exception as e:
        print(e)
    
def remover_lista_conteudo(ctrl: controller_categorias):
    try:
        indice_lista = int(input("Digite o número da lista para deletar: "))
        if indice_lista == 1:
            print("Impossivel deletar a categoria Padrão")
        else:
            lista = ctrl.retornar_categoria(indice_lista-2) # ajuste indice na view
            if ctrl.excluir_categoria(lista):
                print("Categoria excluida com sucesso!!!")
            else:
                print("Não foi possivel excluir a Categoria!")
    except Exception as e:
        print(e)