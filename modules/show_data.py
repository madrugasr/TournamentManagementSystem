import csv, time
from tabulate import tabulate
from modules.tools import limpa_tela, sair


def mostrar_dados():
    """
    Função: Cosultar Dados do Sistema.
    """
    limpa_tela()
    print('\n\033[4;34mMostrar Dados\033[m')

    print('\n1. Dados Introduzidos')
    print('2. Dados Aleatórios')

    op = input('\nOpção: ').strip()
    while op != '1' and op != '2' or op == '':
        print('\n\033[31mOpção Incorreta.\033[m')
        op = input()

    if op == '1':
        lista_mostrar = []
        with open("database/lists/storage/game_data.csv", "r", encoding="utf8") as deletar_dados:
            for linha in csv.reader(deletar_dados):
                lista_mostrar.append(linha)
        lista_mostrar.pop(0)
        print('\n')
        print(tabulate(lista_mostrar, headers=[
              'Jogo', 'Grupo', 'Seleção 1', 'Seleção 2', 'Estádio', 'Espectadores']))
        time.sleep(10)

    elif op == '2':
        lista_mostrar = []
        with open("database/lists/storage/random_game_data.csv", "r", encoding="utf8") as deletar_dados:
            for linha in csv.reader(deletar_dados):
                lista_mostrar.append(linha)
        lista_mostrar.pop(0)
        print('\n')
        print(tabulate(lista_mostrar, headers=[
              'Jogo', 'Grupo', 'Seleção 1', 'Seleção 2', 'Estádio', 'Espectadores']))
        time.sleep(10)

    print('\n\033[1;32m1. Menu Inicial\033[m')
    print('\033[1;32m2. Sair\033[m')

    while True:
        op = input('\nOpção: ').strip()
        if op == '1':
            break
        elif op == '2':
            sair()
        print('\n\033[31mOpção Incorreta.\033[m')
    limpa_tela()
