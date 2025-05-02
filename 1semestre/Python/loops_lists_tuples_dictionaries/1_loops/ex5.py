# 5. Escreva um programa que conte quantos números entre 1 e 100 são pares.

pares = 0
for i in range(1, 101):
    if i % 2 == 0:
        pares += 1

print(f"Quantidade de números pares entre 1 e 100: {pares}")