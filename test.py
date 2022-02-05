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

