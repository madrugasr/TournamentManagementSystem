

import csv
from random import random

from modules.tools import limpa_tela


def gerador_dados_aleatorios():
    """
    Função: Gerador de Dados Aleatorios para o Sistema.
    """

    limpa_tela()
    
    #Listas
    lista_paises = []
    lista_estadios = []
    registro_jogos_ale = []
    letras = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    print('\n\033[1;34mGERAÇÃO DE DADOS ALEATORIOS\033[m')

    quant_jogos_aleatorios = input('\nDeseja gerar quantos Jogos aleatórios? ')
    while not quant_jogos_aleatorios.isnumeric():
        print('\n\033[31mOpção Incorreta.\033[m')
        quant_jogos_aleatorios = input('\nDeseja gerar quantos Jogos aleatórios? ')

    for q in range(int(quant_jogos_aleatorios)):
        #Jogos
        jogos_ale = random.randint(1, 195)
        print('\nJogo:', jogos_ale)
        
        #Grupo
        grupo_ale = random.choice(letras)
        print('Grupo:', grupo_ale)

        #Seleções
        with open("database/lists/reading/coutries.csv","r", encoding="utf8") as f_paises:
            for linha in csv.reader(f_paises):
                lista_paises.append(linha)
        
        #Seleção 1
        selecao1_ale = random.choice(lista_paises)
        print('Seleção 1:', *selecao1_ale)

        #Seleção 2
        selecao2_ale = random.choice(lista_paises)
        print('Seleção 2:', *selecao2_ale)

        #Estádio
        with open('database/lists/reading/stages.csv','r', encoding='utf8') as f_estadios:
            for linha in csv.reader(f_estadios):
                lista_estadios.append(linha)
        estadios_ale = random.choice(lista_estadios)
        print('Estádio:', *estadios_ale)

        #Espectadores
        espectadores_ale = random.randint(20000, 100000)
        print('Espectadores:', espectadores_ale)
    
        registro_jogos_ale.append([jogos_ale, grupo_ale, selecao1_ale, selecao2_ale, estadios_ale, espectadores_ale])

        
    op_gd = input('\nGuardar os Dados: [S/n] ')
    while op_gd != 'S' and op_gd != 'n':
        print('\n\033[31mOpção Incorreta.\033[m')
        op_gd = input('\nGuardar os Dados: [S/n] ') 

    #Guardar Dados Aleatórios
    with open("database/lists/storage/random-game-data.csv","a+", newline='', encoding='utf8') as salvar_dados:
        s = csv.writer(salvar_dados)
        s.writerow(('Jogo',' Grupo',' Seleção 1',' Seleção 2',' Estádio',' Espectadores'))
        s.writerows(registro_jogos_ale)
    print('Dados salvos com sucesso!')
    
    limpa_tela()