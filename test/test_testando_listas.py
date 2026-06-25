import os
import sys
import pytest
# Adiciona a pasta raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models.factory_midia import Factory_Midia
from src.models.tipos_midia import *
from src.models.midia import Midia
#from src.views.view_midia import midia_detalhes
from src.controllers.controller_categorias import controller_categorias



def test_criacao_midia_factory_apenas_autor():
    filme_teste = Factory_Midia.nova_midia("filme 01", "Filme")

    if isinstance(filme_teste, Midia): print("filme criado com sucesso")
    else:  print("filme não foi criado")

    if filme_teste.titulo == "filme 01": print("filme com nome correto")
    else:  print("filme nome erado")

    assert isinstance(filme_teste, Midia)
    assert filme_teste.titulo == "filme 01"
    

def test_criacao_midia_factory_dados_adicionais():
    filme_teste = Factory_Midia.nova_midia("filme 01", "Filme", "cerginho da pereira nunes", "AAAAAAAAA")
    filme_teste.preencher_dados(diretor="Carl Sagan", estudio="Cosmos Studios")
    assert isinstance(filme_teste, Filme)
    assert filme_teste.diretor == "Carl Sagan", "O getter do diretor falhou"
    assert filme_teste.estudio == "Cosmos Studios", "O getter do estudio falhou"
    assert filme_teste.autor == "cerginho da pereira nunes", "O getter do autor falhou"


def test_modificar_midia_em_uma_categoria():
    # Limpa a instância do Singleton para garantir um teste limpo
    controller_categorias._clear_instance() 
    ctlr = controller_categorias()
    ctlr.criar_categoria("nova_categoria")
    
    nova_midia = Factory_Midia.nova_midia("anime", "Anime","eeeeeee", "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
    
    assert isinstance(nova_midia, Midia)
    
    ctlr.append_midia(nova_midia, 0)

    categoria = ctlr.retornar_categoria(0)
    assert nova_midia in categoria._midia, "A mídia não foi adicionada à categoria correta."
    assert nova_midia in ctlr._lista_midias, "A mídia não foi adicionada à lista global."

if __name__ == "__main__":
    test_criacao_midia_factory_apenas_autor()