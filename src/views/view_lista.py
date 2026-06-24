import os
import sys
# Adiciona a pasta raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.controllers.controller_categorias import controller_categorias
from src.models.midia import Midia
from src.views.view_categorias import *
from src.models.factory_midia import Factory_Midia
from src.views.view_midia import *

def listar_conteudos_categoria(controlador: controller_categorias):
    indice = int(input("Digite o número da lista para ver os conteúdos: "))
    try:
        if indice == 1:
            print(controlador.listar_lista_global())
        else:
            lista = controlador.retornar_categoria(indice-2) # ajuste indice na view
            print(lista.listar_conteudo())
        acao = int(input("Deseja fazer alguma ação em alguma mídia?\n"
                     "Digite o indice da midia caso deseje, ENTER caso não deseje: "))
        if acao:
            print(f"{acao-1}")
    except Exception as e:
        print(f"Erro na ação: {e}")

def criar_nova_midia(controlador: controller_categorias):
    try:
        titulo_nova_midia = input("Digite o nome da nova Midia: ")
        autor = input("Digite o nome do autor, ENTER para pular: ")
        comentario = input("Digite um comentário para a midia, ENTER para pular: ")

        tipos_midia = Midia.obter_tipos_midia_existentes()
        msg = f"{'='*30}\nCategorias de Mídia disponíveis:\n"
        for i, nome in enumerate(tipos_midia, 1):
            msg += f"{i} - [{nome}]\n"
        msg += f"{'='*30}"
        tipo = int(input(f"{msg}\nSelecione a desejada: "))

        print(controlador.listar_categorias())
        sel_categoria = int(input(f"\nSelecione uma das listas acima para inserir a Midia: "))

        nova_midia = Factory_Midia.nova_midia(titulo_nova_midia, tipos_midia[tipo-1], autor, comentario) # manda pro factory o class name str
        
        if sel_categoria == 1:
            print(controlador.append_midia(nova_midia))# vai só a midia, salva so na lista padrao
        elif 1 < sel_categoria <= (len(controlador._bibliotecas)+1):
            print(controlador.append_midia(nova_midia, sel_categoria-2))# indice correto no view para evitar problemas em testes
        else:
            raise ValueError("Indice de categoria para inserção inválido")
        midia_detalhes(nova_midia)
        
    except Exception as e:
        print(f"Erro na ação: {e}")
