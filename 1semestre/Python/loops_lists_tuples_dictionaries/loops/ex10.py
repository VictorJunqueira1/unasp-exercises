# 10. Escreva um programa que calcule o fatorial de um número usando laço for.

num = int(input("Insira um número: "))
fatorial = 1
for i in range(1, num + 1):
    fatorial *= i

print(f"O fatorial de {num} é: {fatorial}")