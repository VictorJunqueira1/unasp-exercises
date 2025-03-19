# 14. Elabore um algoritmo que 
# recebe 05 bits individualmente de um número binário
# e mostre o número decimal.

bit1 = int(input("Insira o primeiro bit: "))
bit2 = int(input("Insira o segundo bit: "))
bit3 = int(input("Insira o terceiro bit: "))
bit4 = int(input("Insira o quarto bit: "))
bit5 = int(input("Insira o quinto bit: "))

# Se for 0, não contabiliza o bit

decimal = (bit1 * 2**4) + (bit2 * 2**3) + (bit3 * 2**2) + (bit4 * 2**1) + (bit5 * 2**0)
print(f"O número binário {bit1}{bit2}{bit3}{bit4}{bit5} em decimal é: {decimal}")
