from abc import ABC, abstractmethod
from src.models.midia import Midia
from src.models.tipos_midia import *
from typing import Optional, Literal

class Factory_Midia(ABC): 
    
    @abstractmethod
    def _factory_midia(self, titulo: str, autor: Optional[str] = None, comentario: Optional[str] = None) -> Midia:
        """
        O método factory abstrato. Cada tipo de mídia tem uma classe concreta.
        """
        pass
    
    '''
    Interface para criar a mídia editor sujere 'autor' e 'comentario'.
    '''
    @staticmethod
    def nova_midia(
        titulo: str, 
        tipo: Literal["Anime", "Jogo", "Livro", "Manga", "Filme", "Seriado"], 
        autor: Optional[str] = None,
        comentario: Optional[str] = None
        ) -> Midia:
        
        # usando un dicionario para salvar as factorys concretas disponiveis
        dicionario_factoryes = {
            "Anime": criar_Anime,
            "Jogo": criar_Jogo,
            "Livro": criar_livro,
            "Manga": criar_Manga,
            "Filme": criar_filme,
            "Seriado": criar_seriados
        }
        
        if tipo in dicionario_factoryes:
            # Instancia a factory concreta e chama o método de fabricação passando os argumentos **kwargs
            fabrica_concreta = dicionario_factoryes[tipo]()
            return fabrica_concreta._factory_midia(titulo, autor=autor, comentario=comentario)
            
        raise ValueError(f"Não foi possível criar Mídia: Tipo '{tipo}' é inválido.")

#-------------------------------------------------------------- 
#      Classes concretas dos tipos de mídia
# -------------------------------------------------------------

class criar_Anime(Factory_Midia): 
    def _factory_midia(self, titulo: str, autor: Optional[str] = None, comentario: Optional[str] = None) -> Midia:
        return Anime(titulo, autor, comentario)

class criar_Jogo(Factory_Midia): 
    def _factory_midia(self, titulo: str, autor: Optional[str] = None, comentario: Optional[str] = None) -> Midia:
        return Jogo(titulo, autor, comentario)
    
class criar_livro(Factory_Midia):
    def _factory_midia(self, titulo: str, autor: Optional[str] = None, comentario: Optional[str] = None) -> Midia:
        return Livro(titulo, autor, comentario)
    
class criar_Manga(Factory_Midia):
    def _factory_midia(self, titulo: str, autor: Optional[str] = None, comentario: Optional[str] = None) -> Midia:
        return Manga(titulo, autor, comentario)

class criar_filme(Factory_Midia):
    def _factory_midia(self, titulo: str, autor: Optional[str] = None, comentario: Optional[str] = None) -> Midia:
        return Filme(titulo, autor, comentario)

class criar_seriados(Factory_Midia):
    def _factory_midia(self, titulo: str, autor: Optional[str] = None, comentario: Optional[str] = None) -> Midia:
        return Seriado(titulo, autor, comentario)
