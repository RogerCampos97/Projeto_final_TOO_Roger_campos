from abc import ABC, abstractmethod
from .estado_midia import Estado_Contexto
from .info_datas import Info_data
from typing import Optional

class Midia(ABC):
    """Classe abstrata de midias
    """
    def __init__(self, titulo: str, autor: Optional[str], comentario: Optional[str]):
        self.titulo = titulo
        self._autor = autor
        self.estado = Estado_Contexto()
        self._datas = Info_data()
        self._comentario = comentario
        #self.generos: list[Genero] = []
    
    @property
    def titulo(self):
        return self._titulo
    @property
    def comentario(self):
        return self._comentario
    @property
    def autor(self):
        return self._autor
    
    @titulo.setter
    def titulo(self, add_titulo):
        if not isinstance(add_titulo, str):
            raise TypeError("O nome deve ser texto!")
        add_titulo = " ".join(add_titulo.split())
        if not add_titulo:
            raise ValueError("O nome não pode ser vazio!")
        self._titulo = add_titulo

    @autor.setter
    def autor(self, add_autor):
        if not isinstance(add_autor, str):
            raise TypeError("O nome deve ser texto!")
        add_autor = " ".join(add_autor.split())
        if not add_autor:
            raise ValueError("O nome não pode ser vazio!")
        self._autor = add_autor

    @comentario.setter
    def comentario(self, add_comment):
        if not isinstance(add_comment, str):
            raise TypeError("O nome deve ser texto!")
        add_comment = " ".join(add_comment.split())
        if not add_comment:
            raise ValueError("O nome não pode ser vazio!")
        self.titulo = add_comment


    @abstractmethod
    def __eq__(self, outro:object) -> bool:
        pass
    @abstractmethod
    def get_nome(self) ->str:
        pass

    
    @abstractmethod
    def preencher_dados(
        self, 
        autor: Optional[str] = None, 
        comentario: Optional[str] = None,
        plataforma: Optional[str] = None,
        editora: Optional[str] = None,
        volume: Optional[int] = None,
        estudio: Optional[str] = None,
        diretor: Optional[str] = None,
        temporadas_disponiveis: Optional[int] = None,
	    temporada_assistindo: Optional[int] = None
    ) -> None:""" Método abstrato que força todas as mídias a terem o mesmo setter de dados adicionais
            Todas as classses concretas de midia possuem pelo menos um dos dados adicionais, 
            de acordo com cada tipo ele recebe os dados que precisa.""" 
    pass

    @abstractmethod
    def exibir_detalhes(self):
        return (f"{'='*30}\n[{self.__class__.__name__}]\n"
                f"Titulo: {self._titulo}\n"
                f"Autor: {self._autor if self._autor is not None else "[Desconhecido]"}\n"
                f"Estado: {self.estado.get_nome()}\n"
                f"{self._datas.retorna_todas_datas_formatadas()}\n"
                f"Comentário: {self.comentario if self.comentario is not None else " ..."}\n")
    
    @classmethod
    @abstractmethod
    def campos_disponiveis(cls) -> list[str]:
        pass

    def __str__(self):
        return (f"Nome: {self._titulo} [{self.__class__.__name__}]")
    
    def __repr__(self) -> str:
        return str(self.__dict__)
    
    '''
    @classmethod -> metodo da classe, recebe ela por padrao
    '''
    @classmethod
    def obter_tipos_midia_existentes(cls) -> list:
        '''
        metodo para pegar as classes filhas de midia, precisa do __init__.py 
        com o nome das classes se não retorna lista vazia

            Returns:
                List:
                    Lista com o nome de todos os tipos de Midia(obtido pelo nome da classe)
                    se precisar adicionar mais tipos criar a classe filha, adicionar no factory
                    e no init e a lista atualiza automatico.
        '''
        return [sub.__name__ for sub in cls.__subclasses__()]




