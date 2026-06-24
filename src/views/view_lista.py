import os
import sys
# Adiciona a pasta raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.controllers.controller_categorias import controller_categorias
from src.models.midia import Midia
from src.views.view_categorias import *
from src.models.factory_midia import Factory_Midia
from src.views.view_midia import *

def listar_conteudos_categoria(ctrl: controller_categorias):
    indice_lista = int(input("Digite o número da lista para ver os conteúdos: "))
    try:
        if indice_lista == 1:
            print(ctrl.listar_lista_global())
        else:
            lista = ctrl.retornar_categoria(indice_lista-2) # ajuste indice na view
            print(lista.listar_conteudo())
            indice_midia = int(input("Deseja fazer alguma ação em alguma mídia?\n"
                     "Digite o indice da midia caso deseje, ENTER caso não deseje: "))
            if indice_midia:
                acao = int(input("Selecione a ação:\n"
                     "1 - Ver detalhes\n"
                     "2 - Alterar estado\n"
                     "3 - EXCLUIR A MIDIA\n" \
                     "Selecione: "))
                if acao == 1:
                    midia_detalhes(lista[indice_midia-1])
                elif acao == 2:
                    pass
                elif acao == 3:
                    print(ctrl.remove_midia(lista[indice_midia-1]))

    except Exception as e:
        print(f"Erro na ação: {e}")

def criar_nova_midia(ctrl: controller_categorias):
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

        print(ctrl.listar_categorias())
        sel_categoria = int(input(f"\nSelecione uma das listas acima para inserir a Midia: "))

        nova_midia = Factory_Midia.nova_midia(titulo_nova_midia, tipos_midia[tipo-1], autor, comentario) # manda pro factory o class name str
        
        if sel_categoria == 1:
            print(ctrl.append_midia(nova_midia))# vai só a midia, salva so na lista padrao
        elif 1 < sel_categoria <= (len(ctrl._bibliotecas)+1):
            print(ctrl.append_midia(nova_midia, sel_categoria-2))# indice correto no view para evitar problemas em testes
        else:
            raise ValueError("Indice de categoria para inserção inválido")
        nova_midia = midia_detalhes(nova_midia)
    except Exception as e:
        print(f"Erro na ação: {e}")
