import os
import sys
# Adiciona a pasta raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models import Midia

def midia_detalhes(midia: Midia):
    try:
        print(midia.exibir_detalhes())
        alt = input("Alterar detalhes dessa midia?  1- Sim / enter - Não\nSelecione: ")

    except Exception as e:
            print(f"Erro na ação: {e}")