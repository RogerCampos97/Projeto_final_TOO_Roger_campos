import os
import sys
# Adiciona a pasta raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.models.midia import Midia
from src.models.tipos_midia import *

def midia_detalhes(midia: Midia):
    try:
        while True:
          print(midia.exibir_detalhes())
          alt = int(input("Alterar detalhes dessa midia?  1- Sim / 0 - Não\nSelecione: "))
          if alt == 0:
               print("Retornando para tela anterior...")
               return midia
          elif alt == 1:
               campos = midia.campos_disponiveis()
               coletar_entradas = {}
               print(f"Editando campos de {midia.get_nome()} [{midia.get_tipo()}]")
               for campo in campos:
                    valor = input(f"Digite o valor para [{campo}]: ")
                    if valor:
                         coletar_entradas[campo] = valor
               midia.preencher_dados(**coletar_entradas)
          else:
               raise ValueError("Entrada inválida")
          

    except Exception as e:
          print(f"Erro na ação: {e}")