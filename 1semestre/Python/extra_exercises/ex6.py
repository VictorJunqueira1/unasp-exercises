# 6. Crie 3 varíaveis, solicite que o usuário digite um número
# e verifique se o número digitado pelo usuário
# é maior do que a soma das 3 variáveis

number1 = 10
number2 = 15
number3 = 20

sum = number1 + number2 + number3

number4 = int(input("Digite um número: "))
print(f"Número digitado: {number4}")
print(f"Soma: {sum}")

if number4 > sum:
    print("Número digitado é maior do que a soma")
else: 
    print("Número digitado não é maior do que a soma!")