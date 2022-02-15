from modules.tools import limpa_tela, sair
import csv


def pesquisar_dados():
    """
    Função: Consultar Dados do Sistema.
    """
    limpa_tela()
    print('\n\033[4;34mConsultando Dados\033[m')

    print('\n1. Dados Introduzidos')
    print('2. Dados Aleatórios')

    op = input('\nOpção: ').strip()
    while op != '1' and op != '2' or op == '':
        print('\n\033[31mOpção Incorreta.\033[m')
        op = input()

    if op == '1':
        limpa_tela()
        lista_consultar = []
        with open("database/lists/storage/game_data.csv", "r", encoding="utf8") as deletar_dados:
            for linha in csv.reader(deletar_dados):
                lista_consultar.append(linha)

        j = input('\nJogo: ').strip()
        while not (j.isnumeric()) or int(j) < 1:
            print('\n\033[31mOpção Incorreta.\033[m')
            j = input('\nJogo: ').strip()

        for linha in range(len(lista_consultar)):
            if lista_consultar[linha] == j:
                print(linha)
            else:
                return None

    elif op == '2':
        lista_consultar = []
        with open("database/lists/storage/random_game_data.csv", "r", encoding="utf8") as deletar_dados:
            for linha in csv.reader(deletar_dados):
                lista_consultar.append(linha)

        j = input('\nJogo: ').strip()
        while not (j.isnumeric()) or int(j) < 1:
            print('\n\033[31mOpção Incorreta.\033[m')
            j = input('\nJogo: ').strip()

        for linha in range(len(lista_consultar)):
            if lista_consultar[linha] == j:
                print(linha)
            else:
                return None

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
