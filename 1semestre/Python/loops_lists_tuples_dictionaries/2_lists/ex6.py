# Faça um programa que leia 10 números e crie uma nova lista só com os que são maiores que 50.

lista = []
maiores_que_50 = []

for _ in range(10):
    num = float(input("Insira um número: "))
    lista.append(num)

for num in lista:
    if num > 50:
        maiores_que_50.append(num)

if len(maiores_que_50) == 0:
    print("Não houve números maiores que 50.")
else:
    print(f"Números maiores que 50: {maiores_que_50}")