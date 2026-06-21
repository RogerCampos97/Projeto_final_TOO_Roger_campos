import os
import sys
from typing import List
# Adiciona a pasta raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controllers import Lista_Conteudo
from controllers import controller_categorias
from models import Midia
from view_categorias import *

def listar_conteudos_categoria(controlador: controller_categorias):
    indice = int(input("Digite o número da lista para ver os conteúdos: "))
    try:
        lista = controlador.retornar_categoria(indice)
        if isinstance(lista, int):
            print(controlador.listar_lista_global())
        else:
            print(lista.listar_conteudo())
    except Exception as e:
        print(f"Erro na ação: {e}")

def criar_nova_midia(controlador: controller_categorias):
    try:
        titulo_nova_midia = input("Digite o nome da nova Midia: ")
        tipos_midia = Midia.obter_tipo_midia()
        msg = f"{'='*30}\nCategorias de Mídia disponíveis:\n"
        for i, nome in enumerate(tipos_midia, 1):
            msg += f"{i} - [{nome}]\n"
        msg += f"{'='*30}"
        tipo = int(input(f"{msg}\nSelecione a desejada: "))
        sel_categoria = int(input(f"{listar_categorias(controlador)}\n"
              f"\nSelecione uma das listas acima para inserir a Midia: "))
        
        print(controlador.add_midia(titulo_nova_midia, tipo-1, sel_categoria-2))# indice correto no view para evitar problemas em testes
    except Exception as e:
        print(f"Erro na ação: {e}")


if __name__ == "__main__":
    criar_nova_midia(controlador= controller_categorias())