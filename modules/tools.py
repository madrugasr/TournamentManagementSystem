import sys
from os import name, system


def linha(vezes):
    """
    Função: Linha
    """
    print('\033[1;33m==\033[m' * vezes)


def limpa_tela():
    """
    Função: Limpar a Tela.
    """
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def sair():
    """
    Função: Sair do Sistema.
    """
    limpa_tela()
    sys.exit()
