import os
import sys
# Adiciona a pasta raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models.factory_midia import Factory_Midia
from src.models.midia import Midia


def test_criacao_midia_factory_apenas_autor():
    filme_teste = Factory_Midia.nova_midia("filme 01", "Filme")

    print(filme_teste.estado.get_nome())

    print(filme_teste.exibir_detalhes())


test_criacao_midia_factory_apenas_autor()