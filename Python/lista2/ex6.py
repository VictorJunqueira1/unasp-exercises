# 6. Peça ao usuário para inserir dois números.
# Se a soma dos números for maior que 100, exiba "Soma maior que 100", 
# caso contrário, exiba "Soma menor ou igual a 100".

num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))
result = num1 + num2
print("Soma maior que 100" if result > 100 else "Soma menor ou igual a 100")