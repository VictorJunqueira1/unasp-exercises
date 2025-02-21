# 4. Peça o raio de um círculo e calcule sua área. Em seguida, imprima o resultado.
import math

radius = float(input("Insira o raio do círculo: "))
if radius < 0:
    print("Erro: valor inválido. O raio não pode ser negativo.")
else:
    area = math.pi * radius ** 2
    print(f"A área do círculo é: {area:.2f}")