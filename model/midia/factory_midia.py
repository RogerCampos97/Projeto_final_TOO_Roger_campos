from abc import ABC, abstractmethod
from .midia import Midia


class factory_Midia(ABC):#factory method, responsavel pela criação de cada midia
    def __init__(self, titulo) -> None:
        self.titulo = titulo
   
    @abstractmethod
    def factory_midia(self, titulo) -> Midia:
        """
        O método factory abstrato. Cada tipo de midia tem uma classe concreta 
        que é responsável pela criação de cada tipo de midia.
        feito de acordo com o factory method do site refactoring guru
            Args: titulo
            Returns: objeto do tipo midia
        """
        pass

from .tipos_midia import *    


def nova_midia(titulo: str, tipo: str):
        '''
        aqui logica que define qual tipo de midia vai ser criada
            Args: titulo
            Returns: objeto do tipo midia ou erro caso tipo inválido
        '''
        tipo = tipo.strip().lower()
        match tipo:
            case "anime":
                midia = criar_Anime(titulo).factory_midia(titulo)
            case "jogo":
                midia = criar_Jogo(titulo).factory_midia(titulo)
            case "livro":
                midia = criar_livro(titulo).factory_midia(titulo)
            case "mangá" | "manga":
                midia = criar_Manga(titulo).factory_midia(titulo)
            case "filme":
                midia = criar_filme(titulo).factory_midia(titulo)
            case "seriado" | "seriados":
                midia = criar_seriados(titulo).factory_midia(titulo)
            case _:
                raise Exception("Não foi possivel criar Midia")
        return midia