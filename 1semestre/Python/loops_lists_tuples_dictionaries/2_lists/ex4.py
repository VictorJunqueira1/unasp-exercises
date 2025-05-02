# 4. Crie um programa que leia 5 nomes e armazene em uma lista. Depois, exiba-os em ordem alfabética.

nomes = []
for i in range(5):
    nome = input("Digite um nome: ")
    nomes.append(nome)
    
nomes.sort()
print(nomes)