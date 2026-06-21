from abc import ABC, abstractmethod
from models import Midia
from .tipos_midia import *

class Factory_Midia(ABC): 
    #factory method, responsavel pela criação de cada midia
    def __init__(self, titulo) -> None:
        self.titulo = titulo
   
    @abstractmethod
    def factory_midia(self, titulo) -> Midia:
        """
        O método factory abstrato. Cada tipo de midia tem uma classe concreta 
        que é responsável pela criação de cada tipo de midia.
        feito de acordo com o factory method do site refactoring guru

        ***NÃO DEVE SER CHAMADO DIRETAMENTE, USAR MÉTODO nova_midia***
            
            Args: 
                titulo
            Returns: 
                objeto do tipo midia
        """
        pass
    
    @staticmethod
    def nova_midia(titulo: str, tipo: str):
        '''
        classe usada como interface para criar a midia,
        usa a classe concreta de cada tipo para fazer isso. 
        Aqui fica a logica que define qual tipo de midia vai ser criada

            Args: 
                titulo = nome da midia
                tipo = tipo da midia
            Returns: 
                objeto do tipo midia ou erro caso tipo inválido
        '''
        tipo = tipo.strip().lower()
        match tipo:
            case "anime":
                midia = criar_Anime(titulo).factory_midia(titulo)
            case "jogo":
                midia = criar_Jogo(titulo).factory_midia(titulo)
            case "livro":
                midia = criar_livro(titulo).factory_midia(titulo)
            case "manga":
                midia = criar_Manga(titulo).factory_midia(titulo)
            case "filme":
                midia = criar_filme(titulo).factory_midia(titulo)
            case "seriado":
                midia = criar_seriados(titulo).factory_midia(titulo)
            case _:
                raise Exception("Não foi possivel criar Midia")
        return midia
    
#-------------------------------------------------------------- 
#      Classes concretas dos tipos de midia
# -------------------------------------------------------------
#Anime
class criar_Anime(Factory_Midia): 
    '''classe concreta usada pelo factory para criar o objeto Anime'''
    def factory_midia(self, titulo) -> Midia:
        return Anime(titulo)
#jogo
class criar_Jogo(Factory_Midia): 
    '''classe concreta usada pelo factory para criar o objeto jogo'''
    def factory_midia(self, titulo) -> Midia:
        return Jogo(titulo)
#livro
class criar_livro(Factory_Midia):
    '''classe concreta usada pelo factory para criar o objeto livro'''
    def factory_midia(self, titulo) -> Midia:
        return Livro(titulo)
#mangá 
class criar_Manga(Factory_Midia):
    '''classe concreta usada pelo factory para criar o objeto mangá'''
    def factory_midia(self, titulo) -> Midia:
        return Manga(titulo)
#filme
class criar_filme(Factory_Midia):
    '''classe concreta usada pelo factory para criar o objeto filme'''
    def factory_midia(self, titulo) -> Midia:
        return Filme(titulo)
#seriado
class criar_seriados(Factory_Midia):
    '''classe concreta usada pelo factory para criar o objeto seriado'''
    def factory_midia(self, titulo) -> Midia:
        return Seriado(titulo)




