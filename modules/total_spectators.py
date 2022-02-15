import csv
from modules.tools import limpa_tela, sair


def total_espectadores():
    """
    Função: Total de Espectadores no Campeonato.
    """
    limpa_tela()
    print('\n\033[4;34mTotal Espectadores\033[m')

    print('\n1. Dados Introduzidos')
    print('2. Dados Aleatórios')

    op = input('\nOpção: ').strip()
    while op != '1' and op != '2' or op == '':
        print('\n\033[31mOpção Incorreta.\033[m')
        op = input()
    
    integer = 0
    total_espectadores = []
    if op == '1':
        with open("database/lists/storage/game_data.csv", "r", encoding='utf8') as visualizar:
            for linha in csv.reader(visualizar):
                total_espectadores.append(linha[5].strip())
        total_espectadores.pop(0)
        # Conversão de todos os elementos de uma lista para valores Inteiros.
        for linha in total_espectadores:
            integer = integer + int(linha)
        print(f'\n\033[0;30;44mTotal Espectadores:\033[m {integer}')

    elif op == '2':
        with open("database/lists/storage/random_game_data.csv", "r", encoding="utf8") as visualizar:
            for linha in csv.reader(visualizar):
                total_espectadores.append(linha[5].strip())
        total_espectadores.pop(0)
        # Conversão de todos os elementos de uma lista para valores Inteiros.
        for linha in total_espectadores:
            integer = integer + int(linha)
        print(f'\n\033[0;30;44mTotal Espectadores:\033[m {integer}')

    print('\n\033[1;32m1. Menu Inicial\033[m')
    print('\033[1;32m2. Sair\033[m')
    while True:
        op = input('\nOpção: ').strip()
        if op == '1':
            break
        elif op == '2':
            sair()
        print('\n\033[31mOpção Incorreta.\033[m')