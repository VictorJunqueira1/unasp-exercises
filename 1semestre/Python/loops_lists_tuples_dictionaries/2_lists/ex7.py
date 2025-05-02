# 7. Solicite ao usuário uma palavra e armazene cada letra em uma lista.

palavra = input("Insira uma palavra: ")
letras = []

for letra in palavra:
    letras.append(letra)

print(f"Letras: {letras}")