from abc import ABC, abstractmethod
#from model.midia import Midia

# o estado contexto faz a troca dos estados e o repasse do que deve ser feito para o estado correto
class Estado_Contexto:
    def __init__(self) -> None:
        self._estado_atual = Nao_iniciado()

    def set_estado(self, novo_estado):
        self._estado_atual = novo_estado

    def iniciar(self):
        self._estado_atual.iniciar(self)
    def pausar(self):
        self._estado_atual.pausar(self)
    def concluir(self):
        self._estado_atual.concluir(self)
    def abandonar(self):
        self._estado_atual.abandonar(self)
    def get_nome(self):
        self._estado_atual.get_nome()



class Estado_midia(ABC):    
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
    def abandonar(self, midia):
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

class Nao_iniciado(Estado_midia):
    def get_nome(self):
        return "Não Iniciado"
    
    def iniciar(self, midia):
        pass

    def pausar(self, midia):
        print("Não é possivel pausar, mídia não iniciada")

    def concluir(self, midia):
        midia.set_estado(Em_progresso())

    def abandonar(self, midia):
        midia.set_estado(Abandonado())

class Em_progresso(Estado_midia):
    def get_nome(self):
        return "Em Progresso"
    
    def iniciar(self, midia):
        pass

    def pausar(self, midia):
        pass

    def concluir(self, midia):
        midia.set_estado(Concluido())

class Concluido(Estado_midia):
    def get_nome(self):
        return "Concluído"

class Pausa(Estado_midia):
    def get_nome(self):
        return "Em Pausa"

class Abandonado(Estado_midia):
    def get_nome(self):
        return "Abandonado"
    def iniciar(self, midia):
        pass

    def pausar(self, midia):
        pass

    def concluir(self, midia):
        midia.set_estado(Concluido())
    