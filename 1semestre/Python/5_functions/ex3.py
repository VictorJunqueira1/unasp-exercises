# 3. Crie uma função chamada "calcular_media" que recebe
# uma lista de números como argumento e retorna a média
# aritmética dos elementos.

def calcular_media(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

print(calcular_media([1, 2, 3, 4, 5]))