# 11. Escreva um programa que exiba todos os divisores de um número fornecido pelo usuário.

num = int(input("Insira um número: "))
print("Divisores: ")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)