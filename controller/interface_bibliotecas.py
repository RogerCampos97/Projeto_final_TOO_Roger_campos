from model.biblioteca.gerenciar_biblioteca import Gerenciador_biblioteca


def listar_biblioteca(gerente: Gerenciador_biblioteca):
    print(gerente.listar_bibliotecas())