# 3. Faça um programa que leia o nome de 3 produtos e seus preços, armazenando no dicionário.

produtos = {}
for _ in range(3):
    nome_produto = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: ").replace(",", "."))
    produtos[nome_produto] = preco

print(produtos)