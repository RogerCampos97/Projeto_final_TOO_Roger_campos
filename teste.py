from model.midia.base import Midia
from model.midia.filmes import criar_filme 

#def cria_midia(titulo):


if __name__ == "__main__":
    filme_teste = criar_filme("filme 01")

    print(f"{filme_teste}")
    """ 
    filme_teste.estado_atual.iniciar()
    filme_teste.estado_atual.concluir()
     """
