# 3. Verificar se a palavra é um palíndromo

word = input("Insira uma palavra: ")
reversed_word = word[::-1]

if word == reversed_word:
    print("Palíndromo")
else:
    print("Não é palíndromo")