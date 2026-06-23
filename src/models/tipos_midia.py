from .midia import Midia, AdicionarDadosExtras
from typing import overload
#-------------------------------------------------------------- 
#                   Anime
# -------------------------------------------------------------
class Anime(AdicionarDadosExtras, Midia):
    def __init__(self, titulo, autor, comentario): 
        """ caso não tiver nenhum atributo a mais ou algum codigo
        a ser feito na inicialização posso omitir o init,
        é usado o da classe abstrata """
        super().__init__(titulo, autor, comentario)
        self._estudio: str | None = None
        self._temporadas_disponiveis: int | None = None
        self._temporada_assistindo: int | None = None

    @property
    def estudio(self):
         return self._estudio
    @property
    def temporadas_disponiveis(self):
         return self._temporadas_disponiveis
    @property
    def temporadas_assistindo(self):
         return self.temporadas_assistindo
    
    @estudio.setter
    def estudio (self, nome):
        if not isinstance(nome, str):
            raise TypeError("O nome deve ser texto!")
        nome = " ".join(nome.split())
        if not nome:
            raise ValueError("O nome não pode ser vazio!")
        self._estudio = nome

    @temporadas_assistindo.setter
    def temporadas_assistindo (self, temp):
        if not isinstance(temp, int):
            raise TypeError("volume deve ser numero!")
        if not temp:
            raise ValueError("O nome não pode ser vazio!")
        self._temporadas_assistindo = temp
    
    @temporadas_disponiveis.setter
    def temporadas_disponiveis (self, temp):
        if not isinstance(temp, int):
            raise TypeError("volume deve ser numero!")
        if not temp:
            raise ValueError("O nome não pode ser vazio!")
        self._temporadas_disponiveis = temp

    def preencher_dados(
        self, 
        autor = None, 
        comentario = None, 
        paginas = None, 
        plataforma = None,
        editora = None,
        volume = None,
        estudio = None,
        diretor = None,
        temporadas_disponiveis = None,
	    temporada_assistindo = None
    ) -> None:
        self.estudio = estudio
        self._temporada_assistindo = temporada_assistindo
        self._temporadas_disponiveis = temporadas_disponiveis

    def get_nome(self) -> str:
        return "Anime"
    
    def __eq__(self, outro:object):
        if not isinstance(outro, Anime):
                return False
        return (self.titulo == outro.titulo)
#-------------------------------------------------------------- 
#                   Jogo
# ------------------------------------------------------------- 
class Jogo(AdicionarDadosExtras, Midia):
    def __init__(self, titulo, autor, comentario):
        super().__init__(titulo, autor, comentario)
        self._estudio: str | None = None
        self._plataforma: str | None = None
    
    @property
    def estudio(self):
         return self._estudio
    @property
    def plataforma(self):
         return self._plataforma
    @estudio.setter
    def estudio (self, nome):
        if not isinstance(nome, str):
            raise TypeError("O nome deve ser texto!")
        nome = " ".join(nome.split())
        if not nome:
            raise ValueError("O nome não pode ser vazio!")
        self._estudio = nome
    @plataforma.setter
    def plataforma (self, nome):
        if not isinstance(nome, str):
            raise TypeError("O nome deve ser texto!")
        nome = " ".join(nome.split())
        if not nome:
            raise ValueError("O nome não pode ser vazio!")
        self._plataforma = nome
    
    def preencher_dados(
        self, 
        autor = None, 
        comentario = None, 
        paginas = None, 
        plataforma = None,
        editora = None,
        volume = None,
        estudio = None,
        diretor = None,
        temporadas_disponiveis = None,
	    temporada_assistindo = None
    ) -> None:
        self._plataforma = plataforma
        self._estudio = estudio

    def get_nome(self):
        return "Jogo"
    
    def __eq__(self, outro:object):
        if not isinstance(outro, Jogo):
                return False
        return (self.titulo == outro.titulo)
    
#-------------------------------------------------------------- 
#                   Livro
# -------------------------------------------------------------   
class Livro(AdicionarDadosExtras, Midia):
    def __init__(self, titulo, autor, comentario):
        super().__init__(titulo, autor, comentario)
        self._editora: str | None = None
        self._volumes: int | None = None

    @property
    def editora(self):
         return self._editora
    @property
    def volumes(self):
         return self._volumes
    
    
    @editora.setter
    def editora (self, nome):
        if not isinstance(nome, str):
            raise TypeError("O nome deve ser texto!")
        nome = " ".join(nome.split())
        if not nome:
            raise ValueError("O nome não pode ser vazio!")
        self._editora = nome

    @volumes.setter
    def volumes (self, vol):
        if not isinstance(vol, int):
            raise TypeError("volume deve ser numero!")
        if not vol:
            raise ValueError("O nome não pode ser vazio!")
        self._volumes = vol

    def preencher_dados(
        self, 
        autor = None, 
        comentario = None,
        plataforma = None,
        editora = None,
        volume = None,
        estudio = None,
        diretor = None,
        temporadas_disponiveis = None,
	    temporada_assistindo = None
    ) -> None:
         self._editora = editora
         self._volumes = volume

    def get_nome(self):
        return "Livro"
    def __eq__(self, outro:object):
        if not isinstance(outro, Livro):
                return False
        return (self.titulo == outro.titulo)
#-------------------------------------------------------------- 
#                   Mangá
# -------------------------------------------------------------  
class Manga(AdicionarDadosExtras, Midia):
    def __init__(self, titulo, autor, comentario):
        super().__init__(titulo, autor, comentario)


    def preencher_dados(
        self, 
        autor = None, 
        comentario = None,
        plataforma = None,
        editora = None,
        volume = None,
        estudio = None,
        diretor = None,
        temporadas_disponiveis = None,
	    temporada_assistindo = None
    ) -> None:
         

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

