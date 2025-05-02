# 3. Solicite 10 números ao usuário e exiba a média aritmética.

soma = 0
for _ in range(10):
    num = float(input("Digite um número: "))
    soma += num

media = soma / 10
print(f"A média aritmética dos números digitados é: {media}")