import os
import sys
# Adiciona a pasta raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models.factory_midia import Factory_Midia
from src.models.midia import Midia


def test_criacao_midia_factory_apenas_autor():
    filme_teste = Factory_Midia.nova_midia("filme 01", "Filme")

    if isinstance(filme_teste, Midia): print("midia criada com um so dado")
    else: print("erro na criacao de midia")

    assert isinstance(filme_teste, Midia), "erro na criacao de midia"

def test_criacao_midia_factory_autor_titulo():
    anime_teste = Factory_Midia.nova_midia("anime 01", "Anime", autor="alo")

    if isinstance(anime_teste, Midia): print("midia criada com um dois dados")
    else: print("erro na criacao de midia")

    assert isinstance(anime_teste, Midia), "erro na criacao de midia"

def test_criacao_midia_factory_autor_titulo_comentario():
    manga_teste = Factory_Midia.nova_midia("manga 01", "Manga", autor="carlos antonio", comentario="nada")

    if isinstance(manga_teste, Midia): print("midia criada com um tres dados")
    else: print("erro na criacao de midia")

    assert isinstance(manga_teste, Midia), "erro na criacao de midia"



if __name__ == "__main__":
    test_criacao_midia_factory_apenas_autor()
    test_criacao_midia_factory_autor_titulo()
    test_criacao_midia_factory_autor_titulo_comentario()