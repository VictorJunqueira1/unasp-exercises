# 2. Faça um algoritmo que
# mostre a soma dos dois números positivos mais baixos, 
# dada uma lista de no mínimo 4 números inteiros positivos.

list = [ 25, 42, 12, 18, 22 ] # => 30
smaller1, smaller2 = float('inf'), float('inf')

for num in list:
    if num < smaller1:
        smaller2 = smaller1
        smaller1 = num
    elif num < smaller2:
        smaller2 = num

print(f"A soma dos dois números mais baixos é: {smaller1 + smaller2}")