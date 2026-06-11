from .base import Midia
from .factory_midia import Criador_Midia

class Animes(Midia):
    def __init__(self, titulo: str):
        super().__init__(titulo)

    def get_nome(self):
        return "Animes"
    
    def __str__(self):
        msg = super().__str__()
        msg += (f", {self.__class__.__name__}")
        return msg

class Jogos(Midia):
    def __init__(self, titulo: str):
        super().__init__(titulo)

    def get_nome(self):
        return "Jogos"

    def __str__(self):
        msg = super().__str__()
        msg += (f", {self.__class__.__name__}")
        return msg
class criar_livro(Criador_Midia):
    def criar_midia(self, titulo) -> Midia:
        super().criar_midia(titulo)
        return Livro(titulo)
    
class Livro(Midia):
    def __init__(self, titulo: str):
        super().__init__(titulo)
    
    def get_nome(self):
        return "Livros"

    def __str__(self):
        msg = super().__str__()
        msg += (f", {self.__class__.__name__}")
        return msg
    
class criar_Manga(Criador_Midia):
    def criar_midia(self, titulo) -> Midia:
        super().criar_midia(titulo)
        return Manga(titulo)
    
class Manga(Midia):
    def __init__(self, titulo: str):
        super().__init__(titulo)
    
    def get_nome(self):
        return "Mangás"
    
    def __str__(self):
        msg = super().__str__()
        msg += (f", {self.__class__.__name__}")
        return msg

class filmes(Midia):
    def __init__(self, titulo: str):
        super().__init__(titulo)
    
    def get_nome(self):
        return "Filmes"
    
    def __str__(self):
        msg = super().__str__()
        msg += (f", {self.__class__.__name__}")
        return msg

class criar_filme(Criador_Midia):
    def criar_midia(self, titulo) -> Midia:
        super().criar_midia(titulo)
        return filmes(titulo)

class criar_seriados(Criador_Midia):
    def criar_midia(self, titulo) -> Midia:
        super().criar_midia(titulo)
        return Seriados(titulo)
    
class Seriados(Midia):
    def __init__(self, titulo: str):
        super().__init__(titulo)
    
    def get_nome(self):
        return "Seriados"

    def __str__(self):
        msg = super().__str__()
        msg += (f", {self.__class__.__name__}")
        return msg