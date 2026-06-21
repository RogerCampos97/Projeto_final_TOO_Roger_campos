from .midia import Midia
#-------------------------------------------------------------- 
#                   Anime
# -------------------------------------------------------------
class Anime(Midia):
    def __init__(self, titulo, autor, comentario): 
        """ caso não tiver nenhum atributo a mais ou algum codigo
        a ser feito na inicialização posso omitir o init,
        é usado o da classe abstrata """
        super().__init__(titulo, autor, comentario)
        self._estudio: str | None = None
    @property
    def estudio(self):
         return self._estudio
    @estudio.setter
    def estudio (self, nome):
        if not isinstance(nome, str):
            raise TypeError("O nome deve ser texto!")
        nome = " ".join(nome.split())
        if not nome:
            raise ValueError("O nome não pode ser vazio!")
        self._estudio = nome

    def get_nome(self) -> str:
        return "Anime"
    def __eq__(self, outro:object):
        if not isinstance(outro, Anime):
                return False
        return (self.titulo == outro.titulo)
#-------------------------------------------------------------- 
#                   Jogo
# ------------------------------------------------------------- 
class Jogo(Midia):
    def __init__(self, titulo, autor, comentario):
        super().__init__(titulo, autor, comentario)
        self._estudio: str | None = None
    @property
    def estudio(self):
         return self._estudio
    @estudio.setter
    def estudio (self, nome):
        if not isinstance(nome, str):
            raise TypeError("O nome deve ser texto!")
        nome = " ".join(nome.split())
        if not nome:
            raise ValueError("O nome não pode ser vazio!")
        self._estudio = nome

    def get_nome(self):
        return "Jogo"
    def __eq__(self, outro:object):
        if not isinstance(outro, Jogo):
                return False
        return (self.titulo == outro.titulo)
    
#-------------------------------------------------------------- 
#                   Livro
# -------------------------------------------------------------   
class Livro(Midia):
    def __init__(self, titulo, autor, comentario):
        super().__init__(titulo, autor, comentario)
        self._editora: str | None = None
    @property
    def editora(self):
         return self._editora
    @editora.setter
    def editora (self, nome):
        if not isinstance(nome, str):
            raise TypeError("O nome deve ser texto!")
        nome = " ".join(nome.split())
        if not nome:
            raise ValueError("O nome não pode ser vazio!")
        self._editora = nome

    def get_nome(self):
        return "Livro"
    def __eq__(self, outro:object):
        if not isinstance(outro, Livro):
                return False
        return (self.titulo == outro.titulo)
#-------------------------------------------------------------- 
#                   Mangá
# -------------------------------------------------------------  
class Manga(Midia):
    def __init__(self, titulo, autor, comentario):
        super().__init__(titulo, autor, comentario)
    def get_nome(self):
        return "Mangá"
    def __eq__(self, outro:object):
        if not isinstance(outro, Manga):
                return False
        return (self.titulo == outro.titulo)
#-------------------------------------------------------------- 
#                   Filme
# ------------------------------------------------------------- 
class Filme(Midia):
    def __init__(self, titulo, autor, comentario):
        super().__init__(titulo, autor, comentario)
    def get_nome(self):
        return "Filme"
    def __eq__(self, outro:object):
        if not isinstance(outro, Filme):
                return False
        return (self.titulo == outro.titulo)
#-------------------------------------------------------------- 
#                   Sériados
# ------------------------------------------------------------- 
class Seriado(Midia):
    def __init__(self, titulo, autor, comentario):
        super().__init__(titulo, autor, comentario)
        self._temporadas_disponiveis: int | None = None
        self._temporada_assistindo: int | None = None
        self._diretor: str | None = None
    def get_nome(self):
        return "Seriados"
    def __eq__(self, outro:object):
        if not isinstance(outro, Seriado):
                return False
        return (self.titulo == outro.titulo)

