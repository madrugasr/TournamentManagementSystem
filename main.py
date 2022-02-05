"""
A organização da CBF precisa de um programa de gestão
para a construção do campeonato.

Author: Daniel Marques
"""
#Importando Rescursos.
from fileinput import close
import os
#import numpy as np
import random

def menu():
    """
    Função: Menu de Opções.
    """
    limpa_tela()

    print('\n\033[1;34;40mGestor de Campeonato\033[m')
    print('\n\033[4;32;40mBRASILEIRÃO\033[m')

    print('\n1. Introduzir Dados')
    print('2. Geração de Dados')
    print('3. Alterar Dados')
    print('4. Eliminar Dados')
    print('5. Consultar')
    print('6. Pesquisar')
    print('7. Total de Expectadores')
    print('8. Total de Expectadores por Time')
    print('9. Limpar Tela')
    print('10. Guardar Ficheiro')
    print('11. Carregar dados do Ficheiro')
    print('\033[1;36;40m12. Sobre Nós!\033[m \n')
    print('\033[31m13. Sair\033[m \n')

    linha(20)

    escolha_opcao = int(input('\nDigite sua opção: '))
    #Validação das Opções
    while escolha_opcao < 1 or escolha_opcao > 13:
        print('\n\033[31mResposta Incorreta. Digite novamente!\033[m')
        escolha_opcao = int(input('\nDigite sua opção: '))
        
    #Atribuição de Atitutes
    if escolha_opcao == 1:
        inserir_dados()

    elif escolha_opcao == 2:
        gerador_dados_aleatorios()
    
    elif escolha_opcao == 4:
        eliminar_dados()

    elif escolha_opcao == 9:
        limpa_tela_menu()

    elif escolha_opcao == 10:
        guardar_ficheiro()
    
    elif escolha_opcao == 11:
        carregar_ficheiro()
    
    elif escolha_opcao == 12:
        sobre()
    
    elif escolha_opcao == 13:
        sair()

def inserir_dados():
    """
    Função: Inserir dados no Sistema.
    """
    limpa_tela()

    lista_jogos = [-1]

    print('\n\033[1;34mINSIRA os DADOS\033[m')
    
    while True:
        numero_jogo = input('\nJogo: ')
        while numero_jogo.isnumeric() == False:
            print('\n\033[30;41mDigite o número do Jogo corretamente.\033[m')
            numero_jogo = input('\nJogo: ')
        #numero_jogo = int(numero_jogo)

        while len(lista_jogos) -1 == numero_jogo:
            print(f'\n\033[30;41m{numero_jogo} jogo já existe.\033[m')
            numero_jogo = input('\nJogo: ')

        grupo = input('Grupo: ')
        while any(chr.isdigit() for chr in grupo):
            print('\n\033[30;41mDigite o nome do Grupo corretamente.\033[m')
            grupo = input('\nGrupo: ')

        selecao_1 = input('Seleção 1: ')
        while any(chr.isdigit() for chr in selecao_1):
            print('\n\033[30;41mDigite o nome da Seleção corretamente.\033[m')
            selecao_1 = input('\nSeleção 1: ')


        selecao_2 = input('Seleção 2: ')
        while any(chr.isdigit() for chr in selecao_2):
            print('\n\033[30;41mDigite o nome da Seleção corretamente.\033[m')
            selecao_2 = input('\nSeleção 2: ')

        estadio = input('Estádio: ')
        while any(chr.isdigit() for chr in estadio):
            print('\n\033[30;41mDigite o nome do Estádio corretamente.\033[m')
            estadio = input('\nEstádio: ')

        espectadores = input('Espectadores: ')
        while espectadores.isnumeric() == False:
            print('\n\033[30;41mDigite o númer de Espectadores corretamente.\033[m')
            espectadores = input('\nEspectadores: ')
        
        registro_jogos = [numero_jogo, grupo, selecao_1, selecao_2, estadio, espectadores]
        lista_jogos.append(registro_jogos)

        print(), linha(20)

        print('\n1. Menu Inicial')
        print('2. Inserir próximo Dado')
        op = int(input('\n' ))
        if op == 1:
            limpa_tela(), menu()

def gerador_dados_aleatorios():
    """
    Função: Gerador de Dados Aleatorios.
    """
    limpa_tela()

    print('\n\033[1;34mGERAÇÃO DE DADOS ALEATORIOS\033[m')

    #Gerando número de Jogos aleatórios.
    numero_jogos_ale = random.randint(1, 195)
    print('\nJogo: ', numero_jogos_ale)
    #numero_jogos_ale = np.array([n for n in range (1, 245)])
    #print(numero_jogos_ale)

    #Gerando nome do Grupo aleatórios.
    lista_grupo = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    print('Grupo: ', random.choice(lista_grupo))

    #Gerando nome de Seleções aleatórios.
    ficheiro = open("ficheiro\lista-paises.csv","r", encoding="utf8")
    lista_paises = []

    for linha in ficheiro.readlines():
        lista_paises.append(linha.strip())
    ficheiro.close()
    
    lista_paises_ale = random.choice(lista_paises)
    print('Seleção 1: ', lista_paises_ale)

    lista_paises_ale = random.choice(lista_paises)
    print('Seleção 2: ', lista_paises_ale)


    #tam = len(lista_paises)
    #while len(lista_paises) > 0:
    #   i = random.randint(0, tam-1)
    #   print(lista_paises[i])
    #   lista_paises.pop(i)
    #   tam = len(lista_paises) #atualiza a lista 

    # for posicao in random.randrange(len(lista_paises)):
    #     if lista_paises[posicao]:
    #         print(lista_paises)

def eliminar_dados():
    """
    Função: Eliminar dados do Sistema.
    """
    global lista_jogos

    print('Digite que jogo quer digitar.')

    
def linha(vezes):
    """
    Função: Linha.
    """    
    print('\033[1;33m==\033[m' * vezes)


def limpa_tela_menu():
    """
    Função: Limpar a tela e retorna a Função: Menu.
    """
    if os.name == 'nt':
        os.system('cls')
        menu()
    else:
        os.system('clear')
        menu()

def limpa_tela():
    """
    Função: Limpar a Tela.
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def sair():
    """
    Função: Sair."
    """
    limpa_tela(), close()

def guardar_ficheiro():
    """
    Função: Salvar Ficheiro.
    """

def carregar_ficheiro():
    """
    Função: Carregar Ficheiro.
    """



def sobre():
    """
    Função: Sobre o Programa.
    """
    limpa_tela()
    print("""
    \033[34mSobre Nós!\033[m\n
    Este programa foi desenvolvido a pedido da CBF (Comissão Brasileira de Futebol),
    para atender as necessidades de Gestão dos Campeonatos Brasileiros de Futebol.
    
    \033[35mAuthor:\033[m Daniel Marques.\n""")

    linha(60) 

    opcao = input('\nDeseja voltar ao Menu Inicial? S ou N: ')
    #Validação das Opções
    while opcao != 'S' and opcao != 'N':
        print('\n\033[31mResposta Incorreta. Digite novamente!\033[m')
        opcao = input('\nDeseja voltar ao Menu Inicial? S ou N: ')
    
    if opcao == 'S':
        limpa_tela(), menu()
    elif opcao == 'N':
        limpa_tela(), sair()
        
            

menu()