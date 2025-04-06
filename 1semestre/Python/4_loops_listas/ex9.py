# 9. Faça um algoritmo que determine se há ou não
# caracteres duplos em uma string (incluindo
# caracteres de espaço em branco). Por exemplo aa, !!
# ou (espaço e espaço).
# Mostre True se a string contiver caracteres duplos e
# False se não. O teste não deve diferenciar
# maiúsculas de minúsculas; por exemplo, ambos aa
# e aA mostram True.
# Exemplo:
# "abca" mostra False
# "aabc” mostra True
# "a 11 c d” mostra True
# "AabBcC” mostra True
# "a b  c” mostra True
# "a b c d e f g h i h k” mostra False
# "2020” mostra False
# "a!@€£#$%^&*()_-+=}]{[|\"':;?/>.<,~” mostra False

string = input("Insira uma string: ")

for i in range(len(string) - 1):
    if string[i].lower() == string[i + 1].lower():
        print("True")
        break
else:
    print("False")