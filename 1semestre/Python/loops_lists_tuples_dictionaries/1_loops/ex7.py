# 7. Faça um programa que exiba todos os números ímpares de 1 até um número informado pelo usuário.

limite = int(input("Digite o limite: "))
for i in range(1, limite + 1):
    if i % 2 != 0:
        print(i)