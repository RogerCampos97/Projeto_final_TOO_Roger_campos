from view.menu import Menu, MenuItem
from controller.interface_bibliotecas import *

def main():
    biblioteca = Gerenciador_biblioteca()

    main_menu = Menu("Menu Principal")

    submenu_bibliotecas = Menu("Bibliotecas")
    submenu_bibliotecas.add_item(MenuItem("Listar_bibliotecas", acao=listar_biblioteca(biblioteca)))



    #main_menu.add_item(MenuItem("Bibliotecas", acao=say_hello))
    main_menu.add_item(MenuItem("Serviços", submenu=submenu_bibliotecas))
    #main_menu.add_item(MenuItem("Sobre", acao=show_info))
    main_menu.add_item(MenuItem("Contato", acao=lambda: print("Contato: contato@exemplo.com")))

    main_menu.show()