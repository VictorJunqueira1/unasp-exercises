# 13. Desenvolva um algoritmo que receba do usuário os valores 
# a, b e c, de uma equação do segundo grau 
# (ax^2 + bx + c = 0) e determine as raízes.
import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# (b² - 4ac)
delta = b**2 - 4*a*c

if delta < 0:
    print("A equação não possui raízes reais.")
elif delta == 0:
    x = -b / (2 * a)
    print(f"A equação possui uma raiz real: x = {x}")
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"A equação possui duas raízes reais: x1 = {x1}, x2 = {x2}")