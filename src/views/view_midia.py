import os
import sys
# Adiciona a pasta raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models import Midia
from models.tipos_midia import *

def midia_detalhes(midia: Midia):
    try:
        print(midia.exibir_detalhes())
        alt = int(input("Alterar detalhes dessa midia?  1- Sim / 0 - Não\nSelecione: "))
        if alt == 0:
          print("Saindo...")
        elif alt == 1:
          classe = midia.get_nome()
          campos = midia.campos_disponiveis()
          coletar_entradas = {}
          print(f"Editando campos de {classe.upper()}")
          for campo in campos:
               valor = input(f"Digite o valor para [{campo}]: ")
               coletar_entradas[campo] = valor
          midia.preencher_dados(**coletar_entradas)
        else:
          raise ValueError("Entrada inválida")

    except Exception as e:
          print(f"Erro na ação: {e}")