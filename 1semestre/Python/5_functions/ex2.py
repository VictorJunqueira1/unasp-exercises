# 2. Crie uma função chamada "contador_vogais" que recebe
# uma string como argumento e retorna a quantidade de
# vogais na string.

def contador_vogais(string):
    return sum(1 for char in string if char.lower() in "aeiou")

print(contador_vogais("Oi, tudo bem?"))