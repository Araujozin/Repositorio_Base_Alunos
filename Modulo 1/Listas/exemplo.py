# lista inicial
nome = ["joaquim", "Mauricio", "ana"]
print("Lista inicial:", nome)

# adicionando elementos
nome.append("carlos")  # adiciona ao final
print("Apos append:", nome)

nome.insert(1, "Fernando")  # insere "Fernando" na posição 1
print("Apos insert:", nome)
# Modificando elementos
nome[2] = 'Paulo' # modifica o elementos no índice 2
print('Apos modificação ', nome)

# Removendo elementos
del nome[3] #remove o elementos no índice
print("Após del: ", nome)

nome.remove("Maria") # Remove a primeira ocorrencian de "maria"

removido = nome.pop(2) # Remove e retorna o elemento no indice 2
print(f"apos pop (removido "(removido)"):",nome)

nome.Clear() # Esvazia a lista
print("apos clear:", nome)