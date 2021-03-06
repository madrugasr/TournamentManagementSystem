import csv, time
from modules.tools import limpa_tela, sair

def eliminar_dados():
    """
    Função: Eliminar Dados do Sistema.
    """
    limpa_tela()
    print('\n\033[4;34mEliminar Dados\033[m')

    print('\n1. Dados Introduzidos')
    print('2. Dados Aleatórios')

    op = input('\nOpção: ').strip()
    while op != '1' and op != '2' or op == '':
        print('\n\033[31mOpção Incorreta.\033[m')
        op = input().strip()

    if op == '1':
        lista_deletar_dados = []
        j = input('\nJogo: ')
        while not (j.isnumeric()) or int(j) < 1:
            print('\n\033[31mOpção Incorreta.\033[m')
            j = input('\nJogo: ')

        with open("database/lists/storage/game_data.csv", "r", encoding="utf8") as deletar_dados:
            for linha in csv.reader(deletar_dados):
                lista_deletar_dados.append(linha)
        
        
        print(lista_deletar_dados)
        if j in lista_deletar_dados == False:
            print('\nEsse dado não existe!')

        time.sleep(2)
        print('\n\033[1;33mDado REMOVIDO.\033[m')

    elif op == '2':
        lista_deletar_dados = []
        j = input('\nJogo: ').strip()
        while not (j.isnumeric()) or int(j) < 1:
            print('\n\033[31mOpção Incorreta.\033[m')
            j = input('\nJogo: ').strip()

        lista_deletar_dados = []
        with open("database/lists/storage/random_game_data.csv", "r", encoding="utf8") as deletar_dados:
            for linha in csv.reader(deletar_dados):
                lista_deletar_dados.append(linha)

       
        if j in lista_deletar_dados == False:
            print('\nEsse dado não existe!')
        time.sleep(3)
        print('\n\033[1;33mDado REMOVIDO.\033[m')

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
