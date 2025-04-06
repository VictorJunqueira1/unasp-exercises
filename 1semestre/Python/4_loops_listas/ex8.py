# 8. Dada uma sequência de letras minúsculas ('a' - 'z'),
# obtenha a distância máxima entre duas letras iguais
# e retorne essa distância junto com a letra que a
# formou.
# Caso exista mais de uma letra com a mesma
# distância máxima, retorne a que aparece primeiro.
# Exemplo:
# Para "fffffahhhhhhaaahhhhbhhahhhhabxx", a
# saída deve ser "a23".
# A distância máxima é formada pelo caracter 'a' de
# índice 5 ao índice 27 (baseado em 0). Portanto, a
# saída é "a23".

sequence = "fffffahhhhhhaaahhhhbhhahhhhabxx"

first_indices = {}
max_distance = 0
max_char = None

for i, char in enumerate(sequence):
    if char not in first_indices:
        first_indices[char] = i
    else:
        distance = i - first_indices[char]
        if distance > max_distance:
            max_distance = distance + 1
            max_char = char

print(f"{max_char}{max_distance}")