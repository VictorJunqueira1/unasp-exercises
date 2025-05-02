# 12. Faça um programa que inverta a ordem dos elementos de uma lista.

lista = [1, 2, 3, 4, 5]
lista_invertida = []

for i in range(len(lista) - 1, -1, -1):
    lista_invertida.append(lista[i])

print(f"Lista: {lista}")
print(f"Lista invertida: {lista_invertida}")