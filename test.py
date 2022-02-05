

import random

ficheiro = open("ficheiro\lista-paises.csv","r", encoding="utf8")
lista_paises = []

for linha in ficheiro.readlines():
    lista_paises.append(linha)
    ficheiro.close()
    
random.shuffle(lista_paises)
print(*lista_paises)
print()
print(random.choice(lista_paises))