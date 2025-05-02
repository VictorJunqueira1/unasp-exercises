# 15. Faça um programa que leia uma lista de números e exiba apenas os que estão entre 10 e 50.

import random

lista = [random.randint(1, 100) for _ in range(10)]

print(f"Lista: {lista}")
lista.sort()

for num in lista:
    if num >= 10 and num <= 50:
        print(num)