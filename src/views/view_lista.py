import os
import sys
from typing import List
# Adiciona a pasta raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controllers.controller_lista import Lista_Conteudo
from controllers.controller_categorias import controller_categorias
from models import Midia

def view_listar_conteudos_lista(controlador: controller_categorias):
    indice = int(input("Digite o número da lista para ver os conteúdos: "))
    try:
        lista = controlador.retornar_categoria(indice)
        print(lista.listar_conteudo())
    except Exception as e:
        print(f"Erro na ação: {e}")

def criar_nova_midia(controlador: controller_categorias):
    try:
        nome = input("Digite o nome da nova Midia: ")
        print(f"\nCategorias de Mídia disponíveis: [{Midia.obter_tipo_midia()}]\nSelecione: ")
        

    except Exception as e:
        print(f"Erro na ação: {e}")


