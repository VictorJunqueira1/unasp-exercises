# 6. Escreva um algoritmo que aceite duas
# entradas: message e code, e mostre a mensagem
# oculta, descriptografando a message usando o code.
# O code é um número inteiro não negativo e
# descriptografa em binário a message.
# Exemplos: 
# • Entrada:
# message: “abcdef”
# code: 5
# • Converte o code em binário para
# descriptografar.
# message: “abcdef”
# code: 000101
# • Saída:
# df

message = input("Insira a mensagem: ")
code = int(input("Insira o code: "))

binary_code = bin(code)[2:].zfill(len(message))
result = ""

for i in range(len(message)):
    if binary_code[i] == "1":
        result += message[i]

print(result)