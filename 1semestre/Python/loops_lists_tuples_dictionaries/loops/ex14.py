# 14. Conte quantos números digitados pelo usuário são positivos. O programa deve parar quando um número negativo for digitado.

positivos = 0
while True:
    num = float(input("Insira um número: "))
    if num < 0:
        break
    positivos += 1

print(f"Quantidade de números positivos digitados: {positivos}")