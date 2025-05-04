# 2. Faça um programa que leia 5 números e os armazene em uma tupla. Depois exiba-os em ordem crescente.

numeros = tuple(int(input(f"Digite o {i+1}° número: ")) for i in range(5))
print("Números em ordem crescente:", tuple(sorted(numeros)))