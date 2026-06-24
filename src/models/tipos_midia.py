from src.models.midia import Midia
from typing import overload
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
        self._temporadas_disponiveis: int | None = None
        self._temporadas_assistindo: int | None = None

    @property
    def estudio(self):
         return self._estudio
    @property
    def temporadas_disponiveis(self):
         return self._temporadas_disponiveis
    @property
    def temporadas_assistindo(self):
         return self._temporadas_assistindo
    
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
        temp = int(temp)
        if not isinstance(temp, int):
            raise TypeError("volume deve ser numero!")
        if not temp:
            raise ValueError("O nome não pode ser vazio!")
        self._temporadas_assistindo = temp
    
    @temporadas_disponiveis.setter
    def temporadas_disponiveis (self, temp):
        temp = int(temp)
        if not isinstance(temp, int):
            raise TypeError("volume deve ser numero!")
        if not temp:
            raise ValueError("O nome não pode ser vazio!")
        self._temporadas_disponiveis = temp

    def preencher_dados(
        self, 
        titulo = None,
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
        if titulo is not None: self.titulo = titulo
        if autor is not None: self.autor = autor
        if comentario is not None: self.comentario = comentario
        if estudio is not None: self.estudio = estudio
        if temporada_assistindo is not None: self.temporadas_assistindo = temporada_assistindo
        if temporadas_disponiveis is not None: self.temporadas_disponiveis = temporadas_disponiveis
    
    @classmethod
    def campos_disponiveis(cls) -> list[str]:
        return ["titulo", "autor", "comentario", "estudio", "temporada_assistindo", "temporadas_disponiveis"]

    def get_tipo(self) -> str:
        return "Anime"
    
    def __eq__(self, outro:object):
        if not isinstance(outro, Anime):
                return False
        return (self.titulo == outro.titulo)
    
    def exibir_detalhes(self):
        msg = super().exibir_detalhes()
        msg += (f"Estudio: {self._estudio if self._estudio is not None else "N/A"}\n"
                f"Temporadas assistindo: {self._temporadas_assistindo if self._temporadas_assistindo is not None else "N/A"}\n"
                f"Temporadas disponiveis: {self._temporadas_disponiveis if self._temporadas_disponiveis is not None else "N/A"}\n{'='*30}\n")
        return msg

#-------------------------------------------------------------- 
#                   Jogo
# ------------------------------------------------------------- 
class Jogo(Midia):
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
        titulo = None,
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
        if titulo is not None: self.titulo = titulo
        if autor is not None: self.autor = autor
        if comentario is not None: self.comentario = comentario
        if plataforma is not None: self.plataforma = plataforma
        if estudio is not None: self.estudio = estudio

    @classmethod
    def campos_disponiveis(cls) -> list[str]:
        return ["titulo","autor", "comentario", "plataforma", "estudio"]

    def get_tipo(self):
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
class Livro(Midia):
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
        vol = int(vol)
        if not isinstance(vol, int):
            raise TypeError("volume deve ser numero!")
        if not vol:
            raise ValueError("O nome não pode ser vazio!")
        self._volume = vol

    def preencher_dados(
        self, 
        titulo = None,
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
        if titulo is not None: self.titulo = titulo
        if autor is not None: self.autor = autor
        if comentario is not None: self.comentario = comentario
        if editora is not None: self.editora = editora
        if volume is not None: self.volume = volume

    @classmethod
    def campos_disponiveis(cls) -> list[str]:
        return ["titulo","autor", "comentario", "editora", "volume"]

    def get_tipo(self):
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
class Manga(Midia):
    def __init__(self, titulo, autor, comentario):
        super().__init__(titulo, autor, comentario)
        self._volume: int | None = None

    @property
    def volume(self):
         return self._volume
    
    @volume.setter
    def volume(self, vol):
        vol = int(vol)
        if not isinstance(vol, int):
            raise TypeError("volume deve ser numero!")
        if not vol:
            raise ValueError("O nome não pode ser vazio!")
        self._volume = vol

    def preencher_dados(
        self, 
        titulo = None,
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
        if titulo is not None: self.titulo = titulo
        if autor is not None: self.autor = autor
        if comentario is not None: self.comentario = comentario
        if volume is not None: self.volume = volume
    
    @classmethod
    def campos_disponiveis(cls) -> list[str]:
        return ["titulo", "autor", "comentario", "volume"]

    def get_tipo(self):
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
class Filme(Midia):
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
    def diretor(self, nome):
        if not isinstance(nome, str):
            raise TypeError("O nome deve ser texto!")
        nome = " ".join(nome.split())
        if not nome:
            raise ValueError("O nome não pode ser vazio!")
        self._diretor = nome

    def preencher_dados(
        self, 
        titulo = None,
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
        
        if titulo is not None: self.titulo = titulo
        if autor is not None: self.autor = autor
        if comentario is not None: self.comentario = comentario
        if diretor is not None: self.diretor = diretor
        if estudio is not None: self.estudio = estudio

    @classmethod
    def campos_disponiveis(cls) -> list[str]:
        return ["titulo", "autor", "comentario", "diretor", "estudio"]

    def get_tipo(self):
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
class Seriado(Midia):
    def __init__(self, titulo, autor, comentario):
        super().__init__(titulo, autor, comentario)
        self._temporadas_disponiveis: int | None = None
        self._temporadas_assistindo: int | None = None
        self._diretor: str | None = None
    
    @property
    def temporadas_disponiveis(self):
         return self._temporadas_disponiveis
    @property
    def temporadas_assistindo(self):
         return self._temporadas_assistindo
    @property
    def diretor(self):
        return self._diretor

    @temporadas_assistindo.setter
    def temporadas_assistindo (self, temp):
        temp = int(temp)
        if not isinstance(temp, int):
            raise TypeError("volume deve ser numero!")
        if not temp:
            raise ValueError("O nome não pode ser vazio!")
        self._temporadas_assistindo = temp
    
    @temporadas_disponiveis.setter
    def temporadas_disponiveis (self, temp):
        temp = int(temp)
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
        titulo = None,
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
        if titulo is not None: self.titulo = titulo
        if autor is not None: self.autor = autor
        if comentario is not None: self.comentario = comentario
        if temporadas_disponiveis is not None: self.temporadas_disponiveis = temporadas_disponiveis
        if temporada_assistindo is not None: self.temporadas_assistindo = temporada_assistindo
        if diretor is not None: self.diretor = diretor

    @classmethod
    def campos_disponiveis(cls) -> list[str]:
        return ["titulo", "autor", "comentario", "temporadas_disponiveis", "temporada_assistindo"]

    def get_tipo(self):
        return "Seriados"
    
    def __eq__(self, outro:object):
        if not isinstance(outro, Seriado):
                return False
        return (self.titulo == outro.titulo)

    def exibir_detalhes(self):
        msg = super().exibir_detalhes()
        msg += (f"Diretor: {self._diretor if self._diretor is not None else "N/A"}\n"
                f"Temporadas assistindo: {self._temporadas_assistindo if self._temporadas_assistindo is not None else "N/A"}\n"
                f"Temporadas disponiveis: {self._temporadas_disponiveis if self._temporadas_disponiveis is not None else "N/A"}\n{'='*30}\n")
        return msg
