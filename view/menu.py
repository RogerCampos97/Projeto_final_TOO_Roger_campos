from typing import Callable, List, Optional
'''
    typing = usado para anotar o codigo, não influencia na execucão,
    só ajuda na edicao do codigo e se usar algum programa p/ debug
    list -> lista
    optional -> opcional, pode ser nada ou alguma coisa
    callable -> pode ser 'chamado', por ecemplo uma função ou método. ex: fazer_algo()
'''
class MenuItem:
    '''
    classe de item do menu

        Args: 
            titulo: titulo do menu
            acao: o que é feito quando o item correspondente é selecionado, 
            submenu: submenu desse menu (padrao none, pode ser adicionado depois)
    '''
    def __init__(self, titulo: str, acao: Optional[Callable] = None, submenu: 'Menu' = None):# type: ignore
        self.titulo = titulo
        self.acao = acao
        self.submenu = submenu

    def is_submenu(self) -> bool:
        '''
        testar para ver se é um submenu ou opção comum
        '''
        return self.submenu is not None

class Menu:
    '''
    classe do menu principal
    '''
    def __init__(self, titulo: str, descricao: Optional[str] = None, items: Optional[List[MenuItem]] = None, parent: 'Menu' = None):# type: ignore
        self.titulo = titulo
        self.descricao = descricao
        self.items = items or []
        self.parent = parent

    def add_item(self, item: MenuItem):
        '''
        funcão para adicionar um item ao menu

            Args: 
                item: recebe um item do tipo MenuItem que pode também ser um submenu
        '''
        if item.is_submenu():
            item.submenu.parent = self
        self.items.append(item)

    def show(self):
        '''
        função para mostrar o menu criado
        '''
        while True:
            print(f"\n== {self.titulo} ==")
            if self.descricao is not None and isinstance(self.descricao, str):
                print(f"# {self.descricao}")
            for i, item in enumerate(self.items, start=1):
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

            if 1 <= choice_num <= len(self.items):
                selected = self.items[choice_num - 1]
                if selected.is_submenu():
                    selected.submenu.show()
                elif selected.acao:
                    try:
                        selected.acao()
                    except Exception as e:
                        print(f"Erro na ação: {e}")
                else:
                    print("Opção sem ação definida.")
            else:
                print("Escolha inválida. Tente novamente.")

# Exemplo de uso
""" 
def say_hello():
    print("Olá! Você escolheu dizer olá.")

def show_info():
    print("Informações do sistema... (exemplo)")

def main():
    main_menu = Menu("Menu Principal")

    services_menu = Menu("Serviços")
    services_menu.add_item(MenuItem("Design", acao=lambda: print("Serviço: Design")))
    services_menu.add_item(MenuItem("Desenvolvimento", acao=lambda: print("Serviço: Desenvolvimento")))
    services_menu.add_item(MenuItem("Marketing", acao=lambda: print("Serviço: Marketing")))

    main_menu.add_item(MenuItem("Início", acao=say_hello))
    main_menu.add_item(MenuItem("Serviços", submenu=services_menu))
    main_menu.add_item(MenuItem("Sobre", acao=show_info))
    main_menu.add_item(MenuItem("Contato", acao=lambda: print("Contato: contato@exemplo.com")))

    main_menu.show() 
"""