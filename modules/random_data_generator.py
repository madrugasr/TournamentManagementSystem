import csv, time
from random import randint, choice
from modules.tools import limpa_tela


def gerador_dados_aleatorios():
    """
    Função: Gerador de Dados Aleatorios para o Sistema.
    """

    limpa_tela()
    # Listas
    lista_paises = []
    lista_estadios = []
    registro_jogos_ale = []
    letras = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    print('\n\033[4;34mGERAÇÃO DE DADOS ALEATÓRIOS\033[m')

    quant_jogos_aleatorios = input('\nJogos Aleatórios: ')
    while not (quant_jogos_aleatorios.isnumeric()) or int(quant_jogos_aleatorios) > 60:
        if not quant_jogos_aleatorios.isnumeric():
            print('\n\033[31mOpção Incorreta.\033[m')
        elif int(quant_jogos_aleatorios) > 60:
            print('\n\033[31mNão é possível gerar mais de 60 jogos!\033[m')
        quant_jogos_aleatorios = input('\nJogos Aleatórios: ')

    for q in range(int(quant_jogos_aleatorios)):
        print(f'\n\033[1;32mRegistro: {q+1}\033[m')
        # Jogos
        jogos_ale = randint(1, 60)
        print('Jogo:', jogos_ale)

        # Grupo
        grupo_ale = choice(letras)
        print('Grupo:', grupo_ale)

        # Seleções
        with open("database/lists/reading/coutries.csv", "r", encoding="utf8") as f_paises:
            for linha in csv.reader(f_paises):
                lista_paises.append(linha)

        selecao1_ale = choice(lista_paises)
        print('Seleção 1:', *selecao1_ale)

        selecao2_ale = choice(lista_paises)
        print('Seleção 2:', *selecao2_ale)

        # Estádio
        with open('database/lists/reading/stages.csv', 'r', encoding='utf8') as f_estadios:
            for linha in csv.reader(f_estadios):
                lista_estadios.append(linha)
        estadios_ale = choice(lista_estadios)
        print('Estádio:', *estadios_ale)

        # Espectadores
        espectadores_ale = randint(1, 97000)
        print('Espectadores:', espectadores_ale)

        registro_jogos_ale.append([
            jogos_ale, grupo_ale, *selecao1_ale, *
            selecao2_ale, *estadios_ale, espectadores_ale
        ])
        time.sleep(0.8)

    while True:
        op = input('\nGuardar Dados? [S/n]: ').strip()
        if op == 'n':
            break
        elif op == 'S':
            # Guardar Dados Aleatórios
            with open("database/lists/storage/random_game_data.csv", "w+",
                      newline='', encoding='utf8') as salvar:
                s = csv.writer(salvar)
                s.writerow(('Jogo', ' Grupo', ' Seleção 1',
                            ' Seleção 2', ' Estádio', ' Espectadores'))
                registro_jogos_ale.sort()
                s.writerows(registro_jogos_ale)
                time.sleep(2)
            print('\n\033[1;33mDados SALVOS!\033[m')
            time.sleep(10)
            break
        print('\n\033[31mOpção Incorreta.\033[m')
