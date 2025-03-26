# 2. Faça um algoritmo que
# mostre a soma dos dois números positivos mais baixos, 
# dada uma lista de no mínimo 4 números inteiros positivos.

list = [25, 42, 12, 18, 22]
smaller1, smaller2 = sorted(list)[:2]

print(f"A soma dos dois números mais baixos é: {smaller1 + smaller2}")