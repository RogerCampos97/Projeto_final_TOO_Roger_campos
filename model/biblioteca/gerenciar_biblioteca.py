from model.biblioteca.biblioteca import Lista_Conteudo
from model.midia.midia import Midia

class SingletonMeta(type): 
    '''
    implementação do padrao singleton para garantir que apenas 
    um gerenciador de biblioteca exista, mesmo que outro seja 
    instanciado ele será o mesmo gerenciador.
    '''
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Gerenciador_biblioteca(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self._lista_midias: list[Midia] = []
        self._bibliotecas: list[Lista_Conteudo] = []

    def criar_biblioteca(self, nome: str):
        '''
        criar novo objeto tipo lista_conteudo e faz
        o append na lista do gerenciador

            Args: 
                nome = nome da lista
        '''
        if not isinstance(nome, str):
            raise TypeError("O nome deve ser texto!")
        nome = " ".join(nome.split())
        if not nome:
            raise ValueError("O nome não pode ser vazio!")
        entrada = Lista_Conteudo(nome)
        if entrada not in self._bibliotecas:
            self._bibliotecas.append(entrada)
        else:
            raise ValueError("Já existe Categoria com o mesmo nome") 

    def excluir_biblioteca(self, biblioteca: Lista_Conteudo) -> bool:
        '''
        excluir uma lista da tipo lista_conteudo da lista bibliotecas 

            Args: 
                biblioteca = lista_conteudo
            Returns: 
                true or false
        '''
        try:
            self._bibliotecas.remove(biblioteca)
            return True
        except ValueError:
            return False  # não encontrado

    def buscar_midia_global(self, nome: str):
        '''
        buscar uma midia na lista global de todas as midias disponiveis
            Args: 
                nome = nome da midia
            Returns: 
                objeto do tipo midia ou None
        '''
        for m in self._lista_midias:
            if m.titulo == nome:
                return m
        return None
    
    def listar_bibliotecas(self):
        '''fução para mostrar as listas de midia'''
        msg = "\nColeçóes:\n"
        for i, mdlista in enumerate(self._bibliotecas, 1):
            msg += f"{i} - {mdlista.nome}\n"
        return msg

