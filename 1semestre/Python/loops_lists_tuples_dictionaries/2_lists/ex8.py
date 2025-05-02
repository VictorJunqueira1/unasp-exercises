# 8. Crie um programa que remova os elementos duplicados de uma lista.

import random

lista = [random.randint(1, 10) for _ in range(10)]

print(f"Lista: {lista}")

lista_sem_duplicados = []

for num in lista:
    if num not in lista_sem_duplicados:
        lista_sem_duplicados.append(num)

print(f"Lista sem duplicados: {lista_sem_duplicados}")