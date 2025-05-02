# 8. Escreva um código que solicite nomes até que a palavra "fim" seja digitada, e depois exiba todos os nomes digitados.

nomes = []
while True:
    nome = input("Digite um nome ('fim' para sair): ")
    if nome.lower() == "fim":
        break
    nomes.append(nome)

print("Nomes digitados:")
for nome in nomes:
    print(nome)