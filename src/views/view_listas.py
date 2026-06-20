import os
import sys
# Adiciona a pasta raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#from src.views.menu import Menu, MenuItem
from src.controllers.controller_biblioteca import controller_listas

def view_criar_lista_conteudo(controlador: controller_listas):
        try:
            nova_categoria = input("Digite o nome da nova categoria: ")
            print(controlador.criar_categoria(nova_categoria))
        except Exception as e:
            print(e)
        else:
            print("Categoria criada com sucesso!!!")