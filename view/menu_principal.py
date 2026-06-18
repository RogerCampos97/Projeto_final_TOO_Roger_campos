import os
import sys
# Adiciona a pasta raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controller.interface_bibliotecas import *
from view.menu import Menu, MenuItem

def main():
    biblioteca = categorias()

    main_menu = Menu("Menu Principal")

    submenu_bibliotecas = Menu("Categorias")
    submenu_bibliotecas.add_item(MenuItem("Listar Categorias", acao=biblioteca.listar))
    submenu_bibliotecas.add_item(MenuItem("Criar nova categoria", acao=biblioteca.criar_nova))
    



   
    main_menu.add_item(MenuItem("Categorias", submenu=submenu_bibliotecas))
    main_menu.add_item(MenuItem("Contato", acao=lambda: 
                                print("Contato: contato@exemplo.com")))

    main_menu.show()

if __name__ == "__main__":
    main()