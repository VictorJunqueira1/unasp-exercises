# 9. Crie uma função chamada "encontrar_substring" que
# recebe uma string e uma substring como argumentos, e
# retorna True se a substring estiver presente na string, e
# False caso contrário.

def encontrar_substring(string, substring):
    return substring in string

print(encontrar_substring("abca", "abc"))