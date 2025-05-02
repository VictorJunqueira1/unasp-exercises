# 10. Faça um programa que leia os preços de 5 produtos e exiba a soma e a média.

precos = []
for _ in range(5):
    preco = float(input("Digite o preço do produto: ").replace(",", "."))
    precos.append(preco)

soma = sum(precos)
media = soma / len(precos)

print(f"A soma dos preços dos produtos é: {soma:.2f}")
print(f"A média dos preços dos produtos é: {media:.2f}")