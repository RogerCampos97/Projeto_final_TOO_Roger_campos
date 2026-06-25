import os
import sys
from abc import ABC, abstractmethod
# Adiciona a pasta raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.controllers.controller_categorias import controller_categorias


def test_instanciamento_controlller_categorias_mais_de_uma_vez():
    controller_categorias._clear_instance() 
    gerente = controller_categorias()
    gerentenro2 = controller_categorias()

    if id(gerente) == id(gerentenro2): print("Gerente é um singleton")
    else: print("se aparecer essa mensagem, houve falha no singleton")

    assert id(gerente) == id(gerentenro2), "se aparecer essa mensagem, houve falha no singleton"











    

if __name__ == "__main__":
    test_instanciamento_controlller_categorias_mais_de_uma_vez()