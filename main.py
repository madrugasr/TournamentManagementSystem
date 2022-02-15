# Importando Rescursos.
from modules.about import sobre
from modules.delete_data import eliminar_dados
from modules.querying_data import pesquisar_dados
from modules.show_data import mostrar_dados
from modules.tools import limpa_tela, linha, sair
from modules.insert_date import inserir_dados
from modules.random_data_generator import gerador_dados_aleatorios
from modules.total_spectators import total_espectadores
from modules.total_spectators_team import total_espectadores_time


def menu():
    """
    Função: Menu de Opções.
    """
    limpa_tela()
    print('\n\033[1;34;40mGestor de Campeonato\033[m')
    print('\n\033[4;32;40mCOPA DO MUNDO\033[m')

    print('\n1. Introduzir Dados')
    print('2. Geração de Dados')
    print('3. Alterar Dados')
    print('4. Eliminar Dados')
    print('5. Pesquisar')
    print('6. Visualizar Jogos')
    print('7. Total de Expectadores')
    print('8. Total de Expectadores por Time')
    print('\033[1;36;40m9. Sobre Nós!\033[m \n')
    print('\033[31m10. Sair\033[m \n')

    linha(20)

    escolha_opcao = int(input('\nDigite sua Opção: '))
    # Validação das Opções
    while escolha_opcao < 1 or escolha_opcao > 12:
        print('\n\033[31mResposta Incorreta.\033[m')
        escolha_opcao = int(input('\nDigite sua Opção: '))

    # Atribuição de Atitutes
    if escolha_opcao == 1:
        inserir_dados()
    elif escolha_opcao == 2:
        gerador_dados_aleatorios()
    elif escolha_opcao == 4:
        eliminar_dados()
    elif escolha_opcao == 5:
        pesquisar_dados()
    elif escolha_opcao == 6:
        mostrar_dados()
    elif escolha_opcao == 7:
        total_espectadores()
    elif escolha_opcao == 8:
        total_espectadores_time()
    elif escolha_opcao == 9:
        sobre()
    elif escolha_opcao == 10:
        sair()


while True:
    menu()
