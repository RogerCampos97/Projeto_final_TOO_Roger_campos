from model.biblioteca.gerenciar_biblioteca import Gerenciador_biblioteca

class interface_bibliotecas:
    def __init__(self) -> None:
        self.gerente = Gerenciador_biblioteca()


    def listar(self):
        print("sucesso")
        pass
        #print(self.listar())