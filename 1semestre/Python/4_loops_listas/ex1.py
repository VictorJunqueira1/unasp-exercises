# 1. Dado um array de inteiros, mostre o número que
# aparece um número ímpar de vezes. Sempre haverá 
# apenas um número inteiro que aparece um número
# ímpar de vezes.

# matriz1 = [7]                                     => 7 
# matriz2 = [0]                                     => 0
# matriz3 = [1, 1, 2]                               => 2
# matriz4 = [0, 1, 0, 1, 0]                         => 0

# Redução para O(n): Cada elemento da matriz é processado apenas duas vezes.

matriz5 = [ 1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1 ] # => 4

elements = {}

for num in matriz5:
    if num in elements:
        elements[num] += 1
    else:
        elements[num] = 1

for num, count in elements.items():
    if count % 2 != 0:
        print(f"O número que aparece um número ímpar de vezes na matriz é: {num}")
        break