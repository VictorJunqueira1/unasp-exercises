# 9. Peça ao usuário 5 letras e armazene em uma tupla. Depois exiba as vogais digitadas.

letras = tuple(input("Insira uma letra: ") for _ in range(5))
vogais = ("a", "e", "i", "o", "u")

for letra in letras:
    if letra.lower() in vogais:
        print(f"Vogal encontrada: {letra}")