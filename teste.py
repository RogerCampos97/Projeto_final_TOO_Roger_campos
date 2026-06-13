from model.midia.midia import Midia
from model.midia.factory_midia import nova_midia

#def cria_midia(titulo):


if __name__ == "__main__":
    filme_teste = nova_midia("filme 01", "filme")

    print(f"{filme_teste}")

    filme_teste.estado_atual.iniciar()
    filme_teste.estado_atual.concluir()

