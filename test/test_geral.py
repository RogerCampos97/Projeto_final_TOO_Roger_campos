import os
import sys
# Adiciona a pasta raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models import Factory_Midia
from src.models import Midia


def test_criacao_midia_factory():
    filme_teste = Factory_Midia.nova_midia("filme 01", "filme")

    assert isinstance(filme_teste, Midia), "erro na criacao de midia"