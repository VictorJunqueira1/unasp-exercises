# 8. Peça ao usuário para digitar um número e imprima se é positivo ou negativo.
num = float(input("Insira um número: "))
if num == 0:
    print("0 (Neutro)")
elif num > 0:
    print("Positivo")
else:
    print("Negativo")