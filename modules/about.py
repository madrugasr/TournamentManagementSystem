from modules.tools import limpa_tela, linha, sair


def sobre():
    """
    Função: Sobre o Sistema Gerenciador de Campeonatos.
    """
    limpa_tela()

    print("""
    \033[34mSobre Nós!\033[m\n
    Este programa foi desenvolvido a pedido da FIFA (Federação Internacional de Futebol),
    para atender as necessidades de Gestão dos Campeonatos Mundiais da Copa do Mundo.
    
    \033[35mDesenvolvedor:\033[m Daniel Marques.\n""")

    linha(60)

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
