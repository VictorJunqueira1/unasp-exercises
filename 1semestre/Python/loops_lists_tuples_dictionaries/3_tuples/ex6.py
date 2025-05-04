# 6. Crie uma tupla com 10 números e exiba a soma de todos os elementos.

tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
soma = 0
for num in tupla:
    soma += num
    
print(f"A soma dos números da tupla é: {soma}")