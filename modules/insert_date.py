import csv, time
from modules.tools import limpa_tela, sair


def inserir_dados():
    """
    Função: Inserir dados no Sistema.
    """
    limpa_tela()
    print('\n\033[4;34mINSIRA OS DADOS\033[m')
    # Listas
    lista_jogos = []
    contador = 0
    while True:
        jogo = input('\nJogo: ').strip()
        while not (jogo.isnumeric()) or int(jogo) < 1:
            print('\n\033[30;41mDigite o número do Jogo corretamente.\033[m')
            jogo = input('\nJogo: ').strip()

        grupo = input('Grupo: ').strip()
        while any(c.isdigit() for c in grupo):
            print('\n\033[30;41mDigite o nome do Grupo corretamente.\033[m')
            grupo = input('\nGrupo: ').strip()

        selecao_1 = input('Seleção 1: ').strip()
        while any(c.isdigit() for c in selecao_1):
            print('\n\033[30;41mDigite o nome da Seleção corretamente.\033[m')
            selecao_1 = input('\nSeleção 1: ').strip()

        selecao_2 = input('Seleção 2: ').strip()
        while any(c.isdigit() for c in selecao_2):
            print('\n\033[30;41mDigite o nome da Seleção corretamente.\033[m')
            selecao_2 = input('\nSeleção 2: ').strip()

        estadio = input('Estádio: ').strip()
        while any(c.isdigit() for c in estadio):
            print('\n\033[30;41mDigite o nome do Estádio corretamente.\033[m')
            estadio = input('\nEstádio: ').strip()

        espectadores = input('Espectadores: ').strip()
        while not espectadores.isnumeric():
            print(
                '\n\033[30;41mDigite o númer de Espectadores corretamente.\033[m')
            espectadores = input('\nEspectadores: ').strip()

        lista_jogos.append(
            [jogo, grupo, selecao_1, selecao_2, estadio, espectadores])

        with open("database/lists/storage/game_data.csv", "a+", newline='', encoding='utf8') as salvar_dados:
            s = csv.writer(salvar_dados)
            if contador == 0:
                s.writerow(('Jogo', ' Grupo', ' Seleção 1',
                           ' Seleção 2', ' Estádio', ' Espectadores'))
            lista_jogos.sort()
            s.writerows(lista_jogos)

        while True:
            op = input('\nContinuar [S/n] ').strip()
            if op == 'S':
                break
            elif op == 'n':
                time.sleep(1)
                print('\n\033[1;33mDados SALVOS!\033[m')
                time.sleep(1)
                print('\n\033[1;32m1. Menu Inicial\033[m')
                print('\033[1;32m2. Sair\033[m')
                op = input('\nOpção: ').strip()
                if op == '1':
                    break
                elif op == '2':
                    sair()
                print('\n\033[31mOpção Incorreta.\033[m')
            print('\n\033[31mOpção Incorreta.\033[m')
        break
