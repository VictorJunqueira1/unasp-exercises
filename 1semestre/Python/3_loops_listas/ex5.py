# Dado uma matriz de inteiros,  
# encontre o elemento que aparece com mais frequência na matriz.  
# Se houver vários elementos com a mesma frequência máxima 
# retorne qualquer um deles.

matriz = [ 1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 8, 8, 9, 10, 10, 10, 11 ]

max_count = 0
max_element = None

for num in matriz:
    count = matriz.count(num)
    if count > max_count:
        max_count = count
        max_element = num

print(f"O elemento que aparece com mais frequência na matriz é: {max_element}")