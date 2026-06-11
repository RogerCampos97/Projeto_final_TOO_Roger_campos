from .base import Midia
from .factory_midia import Criador_Midia

class Jogos(Midia):
    def __init__(self, titulo: str):
        super().__init__(titulo)


    def __str__(self):
        msg = super().__str__()
        msg += (f", {self.__class__.__name__}")
        return msg

class Livros(Midia):
    def __init__(self, titulo: str):
        super().__init__(titulo)

    def __str__(self):
        msg = super().__str__()
        msg += (f", {self.__class__.__name__}")
        return msg
    
class Mangas(Midia):
    def __init__(self, titulo: str):
        super().__init__(titulo)
    
    def __str__(self):
        msg = super().__str__()
        msg += (f", {self.__class__.__name__}")
        return msg


class filmes(Midia):
    def __init__(self, titulo: str):
        super().__init__(titulo)
    
    def __str__(self):
        msg = super().__str__()
        msg += (f", {self.__class__.__name__}")
        return msg

class criar_filme(Criador_Midia):
    def criar_midia(self, titulo) -> Midia:
        super().criar_midia(titulo)
        return filmes(titulo)
    
class Seriados(Midia):
    def __init__(self, titulo: str):
        super().__init__(titulo)

    def __str__(self):
        msg = super().__str__()
        msg += (f", {self.__class__.__name__}")
        return msg