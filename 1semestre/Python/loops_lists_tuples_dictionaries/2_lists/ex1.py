# 1. Crie uma lista com 10 números digitados pelo usuário.

lista = []
for _ in range(10):
    num = float(input("Insira um número: "))
    lista.append(num)

print(f"Lista: {lista}")