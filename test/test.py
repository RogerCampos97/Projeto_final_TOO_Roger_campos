import os
import sys
from abc import ABC, abstractmethod
# Adiciona a pasta raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ..src.models.factory_midia import factory_Midia



if __name__ == "__main__":
    filme_teste = factory_Midia.nova_midia("filme 01", "filme")

    print(f"{filme_teste}")

    filme_teste.estado.iniciar()
    filme_teste.estado.concluir()

    print(filme_teste.__repr__())