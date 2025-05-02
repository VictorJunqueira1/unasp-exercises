# 14. Verifique se um número está presente em uma lista.

lista = [1, 2, 3, 4, 5]
num = int(input("Insira um número: "))

if num in lista:
    print(f"O número {num} está na lista.")
else:
    print(f"O número {num} não está na lista.")