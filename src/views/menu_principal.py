import os
import sys
# Adiciona a pasta raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.controllers.controller_categorias import controller_categorias
from src.models.factory_midia import Factory_Midia
from src.views.view_categorias import *
from src.views.view_lista import *
from src.views.menu import Menu, MenuItem

def main():
    ctlr = controller_categorias() # controlador de listas de midias

    ctlr.criar_categoria("nova_categoria")
    nova_midia = Factory_Midia.nova_midia("anime", "Anime","eeeeeee", "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
    ctlr.append_midia(nova_midia, 0)

    main_menu = Menu("Menu Principal", "Salve e catalogue as suas Midias nesse programa!!!")

    # submenu listas
    submenu_listas = Menu("Categorias", acao_desc=listar_categorias, args=[ctlr])
    submenu_listas.add_item(MenuItem("Detalhar alguma Categoria", acao=listar_conteudos_categoria, args=[ctlr]))
    submenu_listas.add_item(MenuItem("Criar nova Categoria", acao=criar_lista_conteudo, args=[ctlr]))
    submenu_listas.add_item(MenuItem("Deletar Categoria", acao=remover_lista_conteudo, args=[ctlr]))

    # submenu midias
    submenu_midias = Menu("Midias")
    submenu_midias.add_item(MenuItem("Adicionar Mídia", acao=criar_nova_midia, args=[ctlr]))
    submenu_midias.add_item(MenuItem("Buscar Midia em toda a Biblioteca", acao=buscar_midia_global, args=[ctlr]))
    submenu_midias.add_item(MenuItem("Me dê uma Midia aleatoria", acao=buscar_midia_random, args=[ctlr]))
    
    

    # itens menu principal
    main_menu.add_item(MenuItem("Categorias", submenu=submenu_listas))
    main_menu.add_item(MenuItem("Midias", submenu=submenu_midias))
    main_menu.add_item(MenuItem("Sobre", acao=lambda: input("# Esse é um programa para salvar as suas mídias!!!\n"
                                "* Através do menu Categorias Você pode criar listas para classificar o suas midias\n"
                                "* Para adicionar midias voce deve usar o menu midias\n"
                                "* Para editar uma midia use o menu de Listas e selecione a desejada\n"
                                "* Muito obrigado por usar esse programa =D\n"
                                "--------- Pressione Enter para continuar..."
                                )))
    

    main_menu.show()

if __name__ == "__main__":
    main()
