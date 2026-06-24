import os
import sys
# Adiciona a pasta raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.controllers.controller_categorias import controller_categorias, Factory_Midia
from src.views.view_categorias import *
from src.views.view_lista import *
from src.views.menu import Menu, MenuItem
from src.models.midia import Midia

def main():
    ctlr = controller_categorias() # controlador de listas de midias

    ctlr.criar_categoria("nova_categoria")
    nova_midia = Factory_Midia.nova_midia("anime", "Anime","eeeeeee", "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
    ctlr.append_midia(nova_midia, 0)

    main_menu = Menu("Menu Principal")

    # submenu listas
    submenu_listas = Menu("Categorias", acao_desc=listar_categorias, args=[ctlr])
    submenu_listas.add_item(MenuItem("Detalhar lista", acao=listar_conteudos_categoria, args=[ctlr]))
    submenu_listas.add_item(MenuItem("Criar nova categoria", acao=criar_lista_conteudo, args=[ctlr]))
    submenu_listas.add_item(MenuItem("Deletar categoria", acao=remover_lista_conteudo, args=[ctlr]))

    # submenu midias
    submenu_midias = Menu("Midias")
    submenu_midias.add_item(MenuItem("Adicionar mídia", acao=criar_nova_midia, args=[ctlr]))
    submenu_midias.add_item(MenuItem("Buscar midia em toda a Biblioteca", acao=buscar_midia_global, args=[ctlr]))
    #submenu_midias.add_item(MenuItem("Buscar midia aleatoria", acao=buscar_midia_global, args=[ctlr]))
    
    

    # itens menu principal
    main_menu.add_item(MenuItem("Categorias", submenu=submenu_listas))
    main_menu.add_item(MenuItem("Midias", submenu=submenu_midias))
    

    main_menu.show()

if __name__ == "__main__":
    main()
