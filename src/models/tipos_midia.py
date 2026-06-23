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
    
    def exibir_detalhes(self):
        msg = super().exibir_detalhes()
        msg += (f"Estudio: {self._estudio if self._estudio is not None else "N/A"}\n"
                f"Temporadas assistindo: {self._temporada_assistindo if self._temporada_assistindo is not None else "N/A"}\n"
                f"Temporadas disponiveis: {self._temporadas_disponiveis if self._temporadas_disponiveis is not None else "N/A"}\n{'='*30}\n")
        return msg

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
    
    def exibir_detalhes(self):
        msg = super().exibir_detalhes()
        msg += (f"Estudio: {self._estudio if self._estudio is not None else "N/A"}\n"
                f"Plataforma: {self._plataforma if self._plataforma is not None else "N/A"}\n{'='*30}\n")
        return msg
    
#-------------------------------------------------------------- 
#                   Livro
# -------------------------------------------------------------   
class Livro(AdicionarDadosExtras, Midia):
    def __init__(self, titulo, autor, comentario):
        super().__init__(titulo, autor, comentario)
        self._editora: str | None = None
        self._volume: int | None = None

    @property
    def editora(self):
         return self._editora
    @property
    def volume(self):
         return self._volume
    
    
    @editora.setter
    def editora (self, nome):
        if not isinstance(nome, str):
            raise TypeError("O nome deve ser texto!")
        nome = " ".join(nome.split())
        if not nome:
            raise ValueError("O nome não pode ser vazio!")
        self._editora = nome

    @volume.setter
    def volume (self, vol):
        if not isinstance(vol, int):
            raise TypeError("volume deve ser numero!")
        if not vol:
            raise ValueError("O nome não pode ser vazio!")
        self._volume = vol

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
        self._volume = volume

    def get_nome(self):
        return "Livro"
    def __eq__(self, outro:object):
        if not isinstance(outro, Livro):
                return False
        return (self.titulo == outro.titulo)
    
    def exibir_detalhes(self):
        msg = super().exibir_detalhes()
        msg += (f"Editora: {self._editora if self._editora is not None else "N/A"}\n"
                f"Volume: {self._volume if self._volume is not None else "N/A"}\n{'='*30}\n")
        return msg
#-------------------------------------------------------------- 
#                   Mangá
# -------------------------------------------------------------  
class Manga(AdicionarDadosExtras, Midia):
    def __init__(self, titulo, autor, comentario):
        super().__init__(titulo, autor, comentario)
        self._volume: int | None = None

    @property
    def volume(self):
         return self._volume
    
    @volume.setter
    def volume(self, vol):
        if not isinstance(vol, int):
            raise TypeError("volume deve ser numero!")
        if not vol:
            raise ValueError("O nome não pode ser vazio!")
        self._volume = vol

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
         self._volume = volume

    def get_nome(self):
        return "Mangá"
    def __eq__(self, outro:object):
        if not isinstance(outro, Manga):
                return False
        return (self.titulo == outro.titulo)
    
    def exibir_detalhes(self):
        msg = super().exibir_detalhes()
        msg += (f"Volume: {self._volume if self._volume is not None else "N/A"}\n{'='*30}\n")
        return msg
#-------------------------------------------------------------- 
#                   Filme
# ------------------------------------------------------------- 
class Filme(AdicionarDadosExtras, Midia):
    def __init__(self, titulo, autor, comentario):
        super().__init__(titulo, autor, comentario)
        self._diretor : str | None = None
        self._estudio : str | None = None

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

    @property
    def diretor(self):
         return self._diretor

    @diretor.setter
    def diretor (self, nome):
        if not isinstance(nome, str):
            raise TypeError("O nome deve ser texto!")
        nome = " ".join(nome.split())
        if not nome:
            raise ValueError("O nome não pode ser vazio!")
        self._diretor = nome

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
        self._diretor = diretor
        self._estudio = estudio
         
    def get_nome(self):
        return "Filme"
    def __eq__(self, outro:object):
        if not isinstance(outro, Filme):
                return False
        return (self.titulo == outro.titulo)
    
    def exibir_detalhes(self):
        msg = super().exibir_detalhes()
        msg += (f"Estudio: {self._estudio if self._estudio is not None else "N/A"}\n"
                f"Diretor: {self._diretor if self._diretor is not None else "N/A"}\n{'='*30}\n")
        return msg
#-------------------------------------------------------------- 
#                   Sériados
# ------------------------------------------------------------- 
class Seriado(AdicionarDadosExtras, Midia):
    def __init__(self, titulo, autor, comentario):
        super().__init__(titulo, autor, comentario)
        self._temporadas_disponiveis: int | None = None
        self._temporada_assistindo: int | None = None
        self._diretor: str | None = None
    
    @property
    def temporadas_disponiveis(self):
         return self._temporadas_disponiveis
    @property
    def temporadas_assistindo(self):
         return self.temporadas_assistindo
    @property
    def diretor(self):
        return self._diretor

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

    @diretor.setter
    def diretor (self, nome):
        if not isinstance(nome, str):
            raise TypeError("O nome deve ser texto!")
        nome = " ".join(nome.split())
        if not nome:
            raise ValueError("O nome não pode ser vazio!")
        self._diretor = nome

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
        self._temporadas_disponiveis = temporadas_disponiveis
        self._temporada_assistindo = temporada_assistindo
        self._diretor = diretor

    def get_nome(self):
        return "Seriados"
    
    def __eq__(self, outro:object):
        if not isinstance(outro, Seriado):
                return False
        return (self.titulo == outro.titulo)

    def exibir_detalhes(self):
        msg = super().exibir_detalhes()
        msg += (f"Diretor: {self._diretor if self._diretor is not None else "N/A"}\n"
                f"Temporadas assistindo: {self._temporada_assistindo if self._temporada_assistindo is not None else "N/A"}\n"
                f"Temporadas disponiveis: {self._temporadas_disponiveis if self._temporadas_disponiveis is not None else "N/A"}\n{'='*30}\n")
        return msg
