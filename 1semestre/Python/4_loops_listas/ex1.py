# 1. Dado um array de inteiros, mostre o número que
# aparece um número ímpar de vezes. Sempre haverá 
# apenas um número inteiro que aparece um número
# ímpar de vezes.

# matriz1 = [7]                                     => 7 
# matriz2 = [0]                                     => 0
# matriz3 = [1, 1, 2]                               => 2
# matriz4 = [0, 1, 0, 1, 0]                         => 0
# matriz5 = [1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1] => 4

# Utilizando O(n²)

matriz = [1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]

contagem = {}

for num in matriz:
    contagem = 0
    for i in matriz:
        if i == num:
            contagem += 1
    if contagem % 2 != 0:
        print(f"O número que aparece um número ímpar de vezes é: {num}")
        break