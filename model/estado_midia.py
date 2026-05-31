from abc import ABC, abstractmethod
#from model.midia import Midia

# o estado contexto faz a troca dos estados e o repasse do que deve ser feito para o estado correto
class Estado_Contexto:
    def __init__(self) -> None:
        self._estado_atual = Estado_nao_iniciado()

    def set_estado(self, novo_estado):
        self._estado_atual = novo_estado

    def iniciar(self):
        self._estado_atual.iniciar(self)
    def pausar(self):
        self._estado_atual.pausar(self)
    def concluir(self):
        self._estado_atual.concluir(self)

class Estado_midia(ABC):
    """     @property 
    def midia(self):
        return self.midia
    
    @midia.setter
    def midia(self, atribuir_midia):
        from model.midia import Midia
        if not isinstance(atribuir_midia, Midia):
            raise TypeError("Erro, objeto não é uma Midia")
        self.midia = atribuir_midia """
    
    @abstractmethod
    def iniciar(self, midia):
        pass
    @abstractmethod
    def pausar(self, midia):
        pass
    @abstractmethod
    def concluir(self, midia):
        pass

    @abstractmethod
    def get_nome(self) -> 'str':
        pass

    def __str__(self):
        return (f"{self.__class__.__name__}")
   
    def __eq__(self, outro:object) -> bool:
        if not isinstance(outro, Estado_midia):
            return False
        return (self.__class__.__name__ == outro.__class__.__name__)

#classes concretas de estados

class Estado_nao_iniciado(Estado_midia):
    def get_nome(self):
        return "Não Iniciado"
    
    def iniciar(self, midia):
        midia.set_estado(Estado_em_progresso())

    def pausar(self, midia):
        pass

    def concluir(self, midia):
        pass

class Estado_em_progresso(Estado_midia):
    def get_nome(self):
        return "Em Progresso"

class Estado_concluido(Estado_midia):
    def get_nome(self):
        return "Concluído"
