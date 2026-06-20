import os
import sys
# Adiciona a pasta raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controllers.controller_listas_conteudo import controller_listas
from views.view_listas import *
from views.menu import Menu, MenuItem

def main():
    controlador_de_listas = controller_listas()

    main_menu = Menu("Menu Principal", descricao="alo povo de sergipe")

    submenu_bibliotecas = Menu("Categorias")
    submenu_bibliotecas.add_item(MenuItem("Listar Categorias", acao=view_listar_listas_conteudo, args=("controlador_de_listas")))
    submenu_bibliotecas.add_item(MenuItem("Criar nova categoria", acao=view_criar_lista_conteudo, args=("controlador_de_listas")))
    

   
    main_menu.add_item(MenuItem("Categorias", submenu=submenu_bibliotecas))
    main_menu.add_item(MenuItem("Contato", acao=lambda: print("Contato: contato@exemplo.com")))

    main_menu.show()

if __name__ == "__main__":
    main()