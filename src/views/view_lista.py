import os
import sys
from typing import List
# Adiciona a pasta raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controllers import Lista_Conteudo
from controllers import controller_categorias
from models import Midia, factory_Midia
from view_categorias import listar_listas_conteudo

def listar_conteudos_lista(controlador: controller_categorias):
    indice = int(input("Digite o número da lista para ver os conteúdos: "))
    try:
        lista = controlador.retornar_categoria(indice)
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
        tipo = tipos_midia[tipo-1]
        nova_midia = factory_Midia.nova_midia(titulo_nova_midia, tipo) # manda pro factory o class name str
        sel_categoria = input(f"{listar_listas_conteudo(controlador)}\n"
              f"\nSelecione uma das listas acima para inserir a Midia: ")
        
        

    except Exception as e:
        print(f"Erro na ação: {e}")


