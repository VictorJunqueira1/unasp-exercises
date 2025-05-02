# 13. Leia uma lista de 10 nomes e remova um nome digitado pelo usuário.

nomes = []
for i in range(10):
    nome = input("Insira um nome: ")
    nomes.append(nome)

nome_remover = input("Insira o nome que deseja remover: ")
nomes.remove(nome_remover)

nomes.sort()
print(f"Lista: {nomes}")