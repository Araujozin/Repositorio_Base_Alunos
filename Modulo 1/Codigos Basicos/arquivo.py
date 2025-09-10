nome=input('digite seu nome')

valor=input('digite o valor do produto')

qtd=input('digite a quantidade')

with open("produtos.txt", "a") as arquivo:
    arquivo.write('nome do prduto'+nome+'valor'+ valor+'quantidade'+ qtd)