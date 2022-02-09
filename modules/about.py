from modules.tools import limpa_tela, linha, sair


def sobre():
    """
    Função: Sobre o Programa.
    """
    limpa_tela()
    print("""
    \033[34mSobre Nós!\033[m\n
    Este programa foi desenvolvido a pedido da FIFA (Federação Internacional de Futebol),
    para atender as necessidades de Gestão dos Campeonatos Mundiais da Copa do Mundo.
    
    \033[35mDesenvolvedor:\033[m Daniel Marques.\n""")

    linha(60) 

    print('\n1. Menu Inicial')
    print('\n2. Sair')

    while True:
        op = input('\nOpção: ').strip()

        if op == '1' or op == '2':
            break

        print('\n\033[31mResposta Incorreta.\033[m')

    limpa_tela()

    if op == '2':
        sair()
