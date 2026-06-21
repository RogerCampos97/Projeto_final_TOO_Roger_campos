import os
import sys
# Adiciona a pasta raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models.factory_midia import Factory_Midia
from src.models.midia import Midia


def test_criacao_midia_factory_apenas_autor():
    filme_teste = Factory_Midia.nova_midia("filme 01", "filme")

    assert isinstance(filme_teste, Midia), "erro na criacao de midia"

def test_criacao_midia_factory_autor_titulo():
    anime_teste = Factory_Midia.nova_midia("anime 01", "anime", autor="alo")

    assert isinstance(anime_teste, Midia), "erro na criacao de midia"