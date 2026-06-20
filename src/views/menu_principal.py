import os
import sys
# Adiciona a pasta raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controllers import controller_categorias
from views.view_categorias import *
from views.view_lista import *
from views import Menu, MenuItem

def teste_chamar(teste):
    print(teste)

def main():
    ct = controller_categorias()

    
    #main_menu = Menu("Menu Principal", acao_desc=teste_chamar, args=["teste2"])
    #main_menu = Menu("Menu Principal", acao_desc="eu fiz funfa")
    main_menu = Menu("Menu Principal")

    # submenu listas
    submenu_listas = Menu("Categorias", acao_desc=listar_categorias, args=[ct])
    submenu_listas.add_item(MenuItem("Detalhar lista", acao=listar_conteudos_categoria, args=[ct]))
    submenu_listas.add_item(MenuItem("Criar nova categoria", acao=criar_lista_conteudo, args=[ct]))

    # submenu midias
    submenu_midias = Menu("Midias")
    submenu_midias.add_item(MenuItem("Adicionar mídia", acao=criar_nova_midia, args=[ct]))
    

    # itens menu principal
    main_menu.add_item(MenuItem("Categorias", submenu=submenu_listas))
    main_menu.add_item(MenuItem("Midias", submenu=submenu_midias))
    main_menu.add_item(MenuItem("Contato", acao=lambda: print("Contato: contato@exemplo.com")))

    main_menu.show()

if __name__ == "__main__":
    main()