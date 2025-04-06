# 5. Crie uma função chamada "encontrar_primos" que recebe
# um número inteiro positivo como argumento e retorna
# uma lista com todos os números primos menores ou iguais
# ao número fornecido.

def encontrar_primos(n):
    primos = []
    for i in range(2, n + 1):
        eh_primo = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                eh_primo = False
                break
        if eh_primo:
            primos.append(i)
    return primos

print(encontrar_primos(10))