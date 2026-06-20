import os
import sys
from abc import ABC, abstractmethod
# Adiciona a pasta raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ..src.controllers.controller_biblioteca import controller_listas


def test_instanciamento_controlller():
    gerente = controller_listas()
    gerentenro2 = controller_listas()

    assert id(gerente) == id(gerentenro2), "se aparecer essa mensagem, houve falha no singleton"

    """ if id(gerente) == id(gerentenro2): # teste copiado do refactoring guru
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.") """