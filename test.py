produto1 = [ "laranja", 10, 0.99]
produto2 = [ "pera", 5, 0.75]
produto3 = [ "kiwi", 4, 0.98]
lista_compras = [ produto1, produto2, produto3]
print(lista_compras)

ficheiro = open("compras.txt","w+")
ficheiro.write("produto; quantidade; preco\n")

for elemento in lista_compras:
    ficheiro.writelines(f"{elemento[0]}; {elemento[1]}; {elemento[2]}\n")
ficheiro.close()   

l = [1,2,3,4,5,5,5,6,6,10,10]
n = input()
for linha in l:
    if linha == n:
        print(19)
print(l)

quant_jogos_aleatorios = input('\nJogos Aleatórios: ')
while not quant_jogos_aleatorios.isnumeric():
    while int(quant_jogos_aleatorios) > 60:
            print('Não é possível gerar mais de 60 jogos!')
            break
    print('\n\033[31mOpção Incorreta.\033[m')
    quant_jogos_aleatorios = input('\nJogos Aleatórios: ')
