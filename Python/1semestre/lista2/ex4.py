# 4. Peça ao usuário para inserir um número.
# Se o número for par, exiba "Número par". Se for ímpar, exiba "Número ímpar".

num = int(input("Insira um número: "))
print("Par" if num % 2 == 0 else "Ímpar")