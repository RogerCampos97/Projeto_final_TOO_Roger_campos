from .midia import Midia
from .factory_midia import factory_Midia

#-------------------------------------------------------------- 
#                   Anime
# -------------------------------------------------------------
class criar_Anime(factory_Midia): 
    # classe concreta usada pelo factory para criar o objeto Anime
    def factory_midia(self, titulo) -> Midia:
        return Anime(titulo)
    
class Anime(Midia):
    def __init__(self, titulo: str): 
        # caso não tiver nenhum atributo a mais ou algum codigo 
        # a ser feito na inicialização posso omitir o init, 
        # é usado o da classe abstrata
        super().__init__(titulo)
    def get_nome(self) -> str:
        return "Anime"
    def __eq__(self, outro:object):
        if not isinstance(outro, Anime):
                return False
        return (self.titulo == outro.titulo)
#-------------------------------------------------------------- 
#                   Jogo
# ------------------------------------------------------------- 
class criar_Jogo(factory_Midia): 
    # classe concreta usada pelo factory para criar o objeto Anime
    def factory_midia(self, titulo) -> Midia:
        return Jogo(titulo)

class Jogo(Midia):
    def __init__(self, titulo: str):
        super().__init__(titulo)
    def get_nome(self):
        return "Jogo"
    def __eq__(self, outro:object):
        if not isinstance(outro, Jogo):
                return False
        return (self.titulo == outro.titulo)
    
#-------------------------------------------------------------- 
#                   Livro
# ------------------------------------------------------------- 
class criar_livro(factory_Midia):
    def factory_midia(self, titulo) -> Midia:
        return Livro(titulo)
    
class Livro(Midia):
    def __init__(self, titulo: str):
        super().__init__(titulo)
    def get_nome(self):
        return "Livro"
    def __eq__(self, outro:object):
        if not isinstance(outro, Livro):
                return False
        return (self.titulo == outro.titulo)
#-------------------------------------------------------------- 
#                   Mangá
# -------------------------------------------------------------  
class criar_Manga(factory_Midia):
    def factory_midia(self, titulo) -> Midia:
        return Manga(titulo)
    
class Manga(Midia):
    def __init__(self, titulo: str):
        super().__init__(titulo)
    def get_nome(self):
        return "Mangá"
    def __eq__(self, outro:object):
        if not isinstance(outro, Manga):
                return False
        return (self.titulo == outro.titulo)
#-------------------------------------------------------------- 
#                   Filme
# ------------------------------------------------------------- 
class criar_filme(factory_Midia):
    def factory_midia(self, titulo) -> Midia:
        return filme(titulo)
    
class filme(Midia):
    def __init__(self, titulo: str):
        super().__init__(titulo)
    def get_nome(self):
        return "Filme"
    def __eq__(self, outro:object):
        if not isinstance(outro, filme):
                return False
        return (self.titulo == outro.titulo)
#-------------------------------------------------------------- 
#                   Sériados
# ------------------------------------------------------------- 
class criar_seriados(factory_Midia):
    def factory_midia(self, titulo) -> Midia:
        return Seriado(titulo)
    
class Seriado(Midia):
    def __init__(self, titulo: str):
        super().__init__(titulo)
    def get_nome(self):
        return "Seriados"
    def __eq__(self, outro:object):
        if not isinstance(outro, Seriado):
                return False
        return (self.titulo == outro.titulo)

