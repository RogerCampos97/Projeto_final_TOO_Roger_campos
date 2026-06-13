from model.midia.factory_midia import factory_Midia

#def cria_midia(titulo):


if __name__ == "__main__":
    filme_teste = factory_Midia.nova_midia("filme 01", "filme")

    print(f"{filme_teste}")

    filme_teste.estado_atual.iniciar()
    filme_teste.estado_atual.concluir()