from modules.tools import limpa_tela, linha


def inserir_dados():
    """
    Função: Inserir dados no Sistema.
    """
    limpa_tela()

    print('\n\033[1;34mINSIRA os DADOS\033[m')

    # Listas
    lista_jogos = []
    while True:
        jogo = input('\nJogo: ')
        while not jogo.isnumeric():
            print('\n\033[30;41mDigite o número do Jogo corretamente.\033[m')
            jogo = input('\nJogo: ')
        lista_jogos.append(jogo)

        while len(lista_jogos) - 1 == jogo:
            print(f'\n\033[30;41m{jogo} jogo já existe.\033[m')
            jogo = input('\nJogo: ')

        grupo = input('Grupo: ')
        while any(c.isdigit() for c in grupo):
            print('\n\033[30;41mDigite o nome do Grupo corretamente.\033[m')
            grupo = input('\nGrupo: ')

        selecao_1 = input('Seleção 1: ')
        while any(c.isdigit() for c in selecao_1):
            print('\n\033[30;41mDigite o nome da Seleção corretamente.\033[m')
            selecao_1 = input('\nSeleção 1: ')

        selecao_2 = input('Seleção 2: ')
        while any(c.isdigit() for c in selecao_2):
            print('\n\033[30;41mDigite o nome da Seleção corretamente.\033[m')
            selecao_2 = input('\nSeleção 2: ')

        estadio = input('Estádio: ')
        while any(c.isdigit() for c in estadio):
            print('\n\033[30;41mDigite o nome do Estádio corretamente.\033[m')
            estadio = input('\nEstádio: ')

        espectadores = input('Espectadores: ')
        while not espectadores.isnumeric():
            print('\n\033[30;41mDigite o númer de Espectadores corretamente.\033[m')
            espectadores = input('\nEspectadores: ')

        registro_jogos = [jogo, grupo, selecao_1, selecao_2, estadio, espectadores]
        lista_jogos.append(registro_jogos)

        print(), linha(20)

        print('\n1. Menu Inicial')
        print('\n2. Continuar')

        while True:
            op = input('\nOpção: ').strip()

            if op == '1' or op == '2':
                break

            print('\n\033[31mResposta Incorreta.\033[m')

        limpa_tela()

        if op == '1':
            break
