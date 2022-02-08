from os import close, name, system
from main import menu

def linha(vezes): """Função: Linha""", print('\033[1;33m==\033[m' * vezes)

def limpa_tela_menu():
    """
    Função: Limpar a tela e retorna a função Menu.
    """
    if name == 'nt': system('cls'), menu()
    else: system('clear'), menu()

def limpa_tela():
    """
    Função: Limpar a Tela.
    """
    if name == 'nt': system('cls')
    else: system('clear')

def sair(): """Função: Sair""", limpa_tela(), close()

def guardar_ficheiro():
    """
    Função: Salvar Ficheiro.
    """

def carregar_ficheiro():
    """
    Função: Carregar Ficheiro.
    """