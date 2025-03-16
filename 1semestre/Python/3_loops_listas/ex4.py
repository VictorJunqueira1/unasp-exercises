# Dada uma matriz de 3x3 preenchida com números inteiros 
# e imprima a soma dos elementos da diagonal principal.

matrix = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]

# 1, 5, 9 -> Tem que somar esses elementos

sum = 0

for i in range(3):
    sum += matrix[i][i]

print(f"A soma dos elementos da diagonal principal é: {sum}")