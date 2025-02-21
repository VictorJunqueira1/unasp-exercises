# 13. Solicite o valor do lado de um quadrado e imprima sua área.
import math

side = float(input("Insira o lado do quadrado: "))
area = math.pow(side, 2)
print(f"A área do quadrado é: {area:.2f}")