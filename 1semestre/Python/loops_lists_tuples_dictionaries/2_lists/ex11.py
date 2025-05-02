# 11. Receba 2 listas de 5 elementos cada e crie uma terceira com a soma dos elementos de mesma posição.

lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]
lista3 = []

for i in range(5):
    lista3.append(lista1[i] + lista2[i])

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Lista 3: {lista3}")