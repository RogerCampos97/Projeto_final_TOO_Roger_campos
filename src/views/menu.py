from typing import Callable, List, Optional
import os
'''
    typing = usado para anotar o codigo, não influencia na execucão 
    só ajuda na edicao do codigo e se usar algum programa p/ debug
    list -> lista
    optional -> opcional, pode ser nada ou alguma coisa
    callable -> pode ser 'chamado', por exemplo uma função ou método. ex: fazer_algo()
'''
class MenuItem:
    '''
    classe de item do menu

        argumentos: 
            titulo: titulo do menu
            acao: o que é feito quando o item correspondente é selecionado, tipo callable(uma função), 
                    passar os argumentos depois em argumentos ou kwargumentos.
            argumentos: argumentos para a funcao enviada no acao
            kwargumentos: kwargumentos para a função enviada no acao
            submenu: submenu desse menu (padrao none)
    '''
    def __init__(self, titulo: str, acao: Optional[Callable] = None, argumentos=(), submenu: 'Menu' = None):# type: ignore
        self.titulo = titulo
        self.acao = acao
        self.argumentos = tuple(argumentos)
        self.submenu = submenu

    def is_submenu(self) -> bool:
        '''
        testar para ver se é um submenu ou opção comum
        '''
        return self.submenu is not None

class Menu:
    '''
    classe do menu principal

        argumentos:
            titulo:
            acao_desc: o que é feito quando o item correspondente é selecionado, tipo callable(uma função), 
                    passar os argumentos depois em argumentos ou kwargumentos, ou um str comum para ser exibido
            argumentos: argumentos para a funcao enviada no acao_desc
            kwargumentos: kwargumentos para a função enviada no acao_desc
            itens: itens do menu, tipo MenuItem
            parent: menu pai
    '''
    def __init__(self, titulo: str, acao_desc: Optional[Callable|str] = None, argumentos=(), 
                 itens: Optional[List[MenuItem]] = None, parent: 'Menu' = None):# type: ignore
        self.titulo = titulo
        self.acao_desc = acao_desc
        self.argumentos = tuple(argumentos)
        self.itens = itens or []
        self.parent = parent

    def add_item(self, item: MenuItem):
        '''
        funcão para adicionar um item ao menu

            argumentos: 
                item: recebe um item do tipo MenuItem que pode também ser um submenu
        '''
        if item.is_submenu():
            item.submenu.parent = self
        self.itens.append(item)

    def show(self):
        '''
        função para mostrar o menu criado
        '''
        while True:
            # Menu.limpar_terminal()
            print(f"\n== {self.titulo} ==")

            try:
                if self.acao_desc is not None:
                    if isinstance(self.acao_desc, str):
                        print(f"# {self.acao_desc}")
                    elif callable(self.acao_desc):
                        self.acao_desc(*self.argumentos)
            except Exception as e:
                print(f"Erro na ação: {e}")

            for i, item in enumerate(self.itens, start=1):
                suffix = " >" if item.is_submenu() else ""
                print(f"{i}. {item.titulo}{suffix}")
            if self.parent:
                print("0. Voltar")
            else:
                print("0. Sair")

            choice = input("Escolha uma opção: ").strip()
            if not choice.isdigit():
                print("Por favor, insira um número válido.")
                continue
            choice_num = int(choice)
            if choice_num == 0:
                if self.parent:
                    return  # volta ao menu pai
                else:
                    print("Saindo...")
                    exit(0) # sair do programa sem erros

            if 1 <= choice_num <= len(self.itens):
                selected = self.itens[choice_num - 1]
                if selected.is_submenu():
                    selected.submenu.show()
                elif selected.acao:
                    try:
                        selected.acao(*selected.argumentos)
                    except Exception as e:
                        print(f"Erro na ação: {e}")
                else:
                    print("Opção sem ação definida.")
                
            else:
                print("Escolha inválida. Tente novamente.")
            if self.parent:
                Menu.pause()
    
    @staticmethod
    def pause():
        input("Pressione Enter para continuar...")
    @staticmethod 
    def limpar_terminal():
        '''
        Função para limpar o terminal, funciona tanto em windows como em mac a principio
        caso não rode comentar a linha abaixo:
        '''
        os.system('cls' if os.name == 'nt' else 'clear')# 'nt': Windows, 'posix': Linux/MacOS
        pass