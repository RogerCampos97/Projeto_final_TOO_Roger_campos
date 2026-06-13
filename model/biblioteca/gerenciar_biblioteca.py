from .biblioteca import Biblioteca
from model.midia.midia import Midia

class Gerenciador_biblioteca:
    def __init__(self) -> None:
        self._lista_midias: list[Midia] = []
        self._bibliotecas: list[Biblioteca] = []

    def criar_biblioteca(self, mome: str):
        pass
    def excluir_biblioteca(self, biblioteca: Biblioteca):
        pass
    def buscar_midia_global(self, midia: Midia):
        pass
    

