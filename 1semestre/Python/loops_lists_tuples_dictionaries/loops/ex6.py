# 6. Crie um programa que leia vários números até que o usuário digite 0 e mostre a soma dos números lidos.

soma = 0
while True:
    num = float(input("Digite um número (0 para sair): "))
    if num == 0:
        break
    soma += num

print(f"A soma dos números digitados é: {soma}")