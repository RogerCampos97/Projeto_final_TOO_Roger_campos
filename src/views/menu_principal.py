import os
import sys
# Adiciona a pasta raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controllers.controller_categorias import controller_categorias
from views.view_categorias import *
from views.menu import Menu, MenuItem

def teste_chamar(teste):
    print(teste)

def main():
    categorias = controller_categorias()

    
    #main_menu = Menu("Menu Principal", acao_desc=teste_chamar, args=["teste2"])
    #main_menu = Menu("Menu Principal", acao_desc="eu fiz funfa")
    main_menu = Menu("Menu Principal")

    submenu_listas = Menu("Categorias", acao_desc=view_listar_listas_conteudo, args=[categorias])
    submenu_listas.add_item(MenuItem("Criar nova categoria", acao=view_criar_lista_conteudo, args=[categorias]))

    submenu_midias = Menu("Midias")
    #submenu_midias.add_item(MenuItem("Listar todas as Mídias", acao=))
    

   
    main_menu.add_item(MenuItem("Categorias", submenu=submenu_listas))
    main_menu.add_item(MenuItem("Midias", submenu=submenu_midias))
    main_menu.add_item(MenuItem("Contato", acao=lambda: print("Contato: contato@exemplo.com")))

    main_menu.show()

if __name__ == "__main__":
    main()