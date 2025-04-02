# 3. As máquinas ATM permitem códigos PIN de 4 ou 6
# dígitos e os códigos PIN não podem conter nada além
# de exatamente 4 ou exatamente 6 dígitos numéricos.
# Faça um algoritmo que o usuário digite o PIN e
# mostre se é uma sequência válida.

pin = input("Insira o PIN: ")

if len(pin) == 4 or len(pin) == 6:
    for i in range(len(pin)):
        if not pin[i].isdigit():
            print("PIN inválido")
            break
    else:
        print("PIN válido")
else:
    print("PIN inválido")