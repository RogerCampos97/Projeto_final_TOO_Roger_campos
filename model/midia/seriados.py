from .base import Midia

class Seriados(Midia):
    def __init__(self, titulo: str):
        super().__init__(titulo)

    def __str__(self):
        msg = super().__str__()
        msg += (f", {self.__class__.__name__}")
        return msg