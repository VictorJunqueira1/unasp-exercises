# 10. Crie um programa que recebe três números do usuário 
# e determina qual é o maior número, utilizando apenas condicionais.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 > num2 and num1 > num3:
    print(f"{num1} é o maior número.")
elif num2 > num1 and num2 > num3:
    print(f"{num2} é o maior número.")
else: 
    print(f"{num3} é o maior número")
    
"""
    1. Outra solução:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))

    bigger = max(num1, num2, num3)
    print(f"{bigger} é o bigger número.")
"""