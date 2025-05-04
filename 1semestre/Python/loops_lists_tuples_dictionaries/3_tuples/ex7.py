# 7. Leia uma tupla com 5 números e exiba a quantidade de números pares.

tupla = (1, 2, 3, 4, 5)
pares = 0
for num in tupla:
    if num % 2 == 0:
        pares += 1

print(f"Quantidade de números pares na tupla: {pares}")