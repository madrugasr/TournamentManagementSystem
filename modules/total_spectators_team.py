import csv
from modules.tools import limpa_tela, sair


def total_espectadores_time():
    """
    Função: Total de Espectadores no Campeonato por Time.
    """
    limpa_tela()
    print('\n\033[4;34mTotal Espectadores por Time\033[m')
    total_espectadores = []
    with open("database/lists/storage/random_game_data.csv", "r", encoding='utf8') as ler_dados:
        for linha in csv.reader(ler_dados):
            total_espectadores.append(linha[5].strip())
    total_espectadores.pop(0)

    with open("database/lists/storage/random_game_data.csv", "r", encoding='utf8') as ler_dados:
        for linha in csv.reader(ler_dados):
            total_espectadores.append(linha[5].strip())
    total_espectadores.pop(0)

    # Conversão de todos os elementos de uma lista para valores Inteiros.
    integer = 0
    for linha in total_espectadores:
        integer = integer + int(linha)
    print(f'\n\033[0;30;44mTotal Espectadores Por Time:\033[m {integer}')

    print('\n\033[1;32m1. Menu Inicial\033[m')
    print('\033[1;32m2. Sair\033[m')
    while True:
        op = input('\nOpção: ').strip()
        if op == '1':
            break
        elif op == '2':
            sair()
        print('\n\033[31mOpção Incorreta.\033[m')
