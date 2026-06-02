from model.midia.base import Midia
from model.midia import filmes



if __name__ == "__main__":
    livro_teste = Midia("livro 1")

    print(f"{livro_teste}")

    #livro_teste.estado_atual.iniciar()
    livro_teste.estado_atual.concluir()
    
