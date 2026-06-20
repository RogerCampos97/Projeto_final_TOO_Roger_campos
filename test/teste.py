from src.model.midia.factory_midia import factory_Midia



if __name__ == "__main__":
    filme_teste = factory_Midia.nova_midia("filme 01", "filme")

    print(f"{filme_teste}")

    filme_teste.estado.iniciar()
    filme_teste.estado.concluir()

    print(filme_teste.__repr__())

    from view.menu import main

    # if __name__ == "__main__":
    main()