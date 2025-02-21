# 9. Solicite um valor em reais e imprima o equivalente em dólares (considere a cotação fixa).
real = float(input("Insira um valor em reais: "))
if real < 0:
    print("Erro: valor inválido. Por favor, insira um valor positivo.")
else:
    dollar = real / 5.50
    print(f"{real} reais equivalem a {dollar:.2f} dólares (USD)")