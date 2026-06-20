import os
import sys
from typing import List
# Adiciona a pasta raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controllers.controller_lista import Lista_Conteudo
from controllers.controller_categorias import controller_categorias

def view_listar_conteudos_lista(controlador: controller_categorias):
    indice = int(input("Digite o número da lista para ver os conteúdos: "))
    try:
        lista = controlador.retornar_categoria(indice)
        print(lista.listar_conteudo)
    except Exception as e:
        print(f"Erro na ação: {e}")




