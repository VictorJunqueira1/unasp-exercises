# 9. Faça um programa que conte a frequência de letras em uma palavra usando um dicionário.

palavra = input("Insira uma palavra: ")
frequencia = {}

for letra in palavra:
    if letra in frequencia:
        frequencia[letra] += 1
    else:
        frequencia[letra] = 1

print(frequencia)