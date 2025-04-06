# 5. Crie uma função chamada "encontrar_primos" que recebe
# um número inteiro positivo como argumento e retorna
# uma lista com todos os números primos menores ou iguais
# ao número fornecido.
import timeit

# Versão simples (verifica até i-1)
def encontrar_primos_simples(n):
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

# Versão com Crivo de Eratóstenes
def encontrar_primos_crivo(n):
    if n < 2:
        return []

    primos = [True] * (n + 1)
    primos[0] = primos[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if primos[i]:
            for j in range(i * i, n + 1, i):
                primos[j] = False

    return [i for i, eh_primo in enumerate(primos) if eh_primo]

# Tempo de execução para n = 100_000
tempo_simples = timeit.timeit(lambda: encontrar_primos_simples(100_000), number=1)
tempo_crivo = timeit.timeit(lambda: encontrar_primos_crivo(100_000), number=1)

tempo_simples, tempo_crivo

print(tempo_crivo)
print(tempo_simples)