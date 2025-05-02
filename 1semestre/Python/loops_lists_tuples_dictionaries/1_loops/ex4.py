# 4. Faça um programa que leia um número e exiba sua tabuada de multiplicação (1 a 10).

num = int(input("Insira um número: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")