# 6. Crie uma função chamada "contar_ocorrencias" que
# recebe uma lista de elementos e um elemento específico
# como argumentos, e retorna a quantidade de vezes que o
# elemento aparece na lista.

def contar_ocorrencias(lista, elemento):
    return lista.count(elemento)

print(contar_ocorrencias([1, 2, 3, 4, 5], 3))