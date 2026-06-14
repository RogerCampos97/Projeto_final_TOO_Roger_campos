from model.biblioteca.gerenciar_biblioteca import Gerenciador_biblioteca

gerente = Gerenciador_biblioteca()
gerentenro2 = Gerenciador_biblioteca()

if id(gerente) == id(gerentenro2): # teste copiado do refactoring guru
    print("Singleton works, both variables contain the same instance.")
else:
    print("Singleton failed, variables contain different instances.")